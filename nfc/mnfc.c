/*
	Mifare NFC Python Module for Heiko
	Copyright (C) 2019  Christian Carlowitz <chca@cmesh.de>

	This program is free software: you can redistribute it and/or modify it
	under the terms of the GNU Lesser General Public License as published by the
	Free Software Foundation, either version 3 of the License, or (at your
	option) any later version.

	This program is distributed in the hope that it will be useful, but WITHOUT
	ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
	FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License
	for more details.

	You should have received a copy of the GNU Lesser General Public License
	along with this program.  If not, see <http://www.gnu.org/licenses/>
*/

#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#include <nfc/nfc.h>
#include <freefare.h>

#include <Python.h>

MifareClassicKey default_keys[] = {
    { 0xff,0xff,0xff,0xff,0xff,0xff },
    { 0xd3,0xf7,0xd3,0xf7,0xd3,0xf7 },
    { 0xa0,0xa1,0xa2,0xa3,0xa4,0xa5 },
    { 0xb0,0xb1,0xb2,0xb3,0xb4,0xb5 },
    { 0x4d,0x3a,0x99,0xc3,0x51,0xdd },
    { 0x1a,0x98,0x2c,0x7e,0x45,0x9a },
    { 0xaa,0xbb,0xcc,0xdd,0xee,0xff },
    { 0x00,0x00,0x00,0x00,0x00,0x00 }
};

nfc_device* device = 0;
nfc_context* context = 0;

static PyObject* mnfc_init(PyObject* self, PyObject* args)
{
	const int devicesLen = 8;
	nfc_connstring devices[devicesLen];
	size_t ndev;

	nfc_init(&context);
	if(!context)
	{
		printf("NFC: unable to init libnfc\n");
		return Py_BuildValue("i",0);
	}

	ndev = nfc_list_devices(context, devices, devicesLen);
	if(ndev <= 0)
	{
		printf("NFC: no device found\n");
		return Py_BuildValue("i",0);
	}

	int devFound = 0;
	for (size_t d = 0; d < ndev; d++)
	{
		device = nfc_open(context, devices[d]);
		if(!device)
		{
			printf("NFC: nfc_open() failed\n");
			continue;
		}
		devFound = 1;
		break;
	}
	
	return Py_BuildValue("i", devFound);
}

static PyObject* mnfc_deinit(PyObject* self, PyObject* args)
{
	if(device)
		nfc_close(device);
	if(context)
	    nfc_exit(context);
   	return Py_BuildValue("i", 1);
}

static PyObject* mnfc_read(PyObject* self, PyObject* args)
{
	int ret = 0;
	MifareClassicBlock* block = malloc(sizeof(MifareClassicBlock)*4);
	
	int blockNum;
	PyArg_ParseTuple(args, "i", &blockNum);
	
	#define MAX_UID_LEN 16
	char firstTagUid[MAX_UID_LEN+1] = {0};
	#define MAX_TTYPE_LEN 32
	char firstTagType[MAX_TTYPE_LEN+1] = {0};

Py_BEGIN_ALLOW_THREADS

	MifareTag* tags = freefare_get_tags(device);
	if(!tags)
	{
		printf("NFC: device error while listing tags\n");
		ret = 1;
		goto error;
	}

	for (int i = 0; tags[i]; i++)
	{
		char* tag_uid = freefare_get_tag_uid(tags[i]);
		const char* ttype = freefare_get_tag_friendly_name(tags[i]);
		if(i == 0)
		{
			strncpy(firstTagUid, tag_uid, MAX_UID_LEN);
			strncpy(firstTagType, ttype, MAX_TTYPE_LEN);
		}
		else
		{
			printf("NFC: warning: found additional tag %s with UID %s\n", ttype, tag_uid);
		}
		free(tag_uid);
	}

	if(tags[0])
	{
		if(mifare_classic_connect(tags[0]))
		{
			printf("NFC: mifare_classic_connect failed\n");
			ret = 2;
			goto error;
		}

		MifareClassicBlockNumber b = blockNum*4;
		if(mifare_classic_authenticate(tags[0], b, default_keys[0], MFC_KEY_A))
		{
			printf("NFC: auth failed\n");
			ret = 3;
			goto error;
		}

		for(int k = 0; k < 4; k++)
		{
			int n = mifare_classic_read(tags[0], b+k, &block[k]);
			if(n < 0)
			{
				printf("NFC: read error\n");
				ret = 4;
				goto error;
			}
		}
	}
	else
	{
		ret = 5;
	}

error:
	freefare_free_tags(tags);
	
Py_END_ALLOW_THREADS

	if(!ret)
	{
		PyObject* o = Py_BuildValue("issy#",
			ret, firstTagUid, firstTagType,
			(const char*)block, sizeof(MifareClassicBlock)*4);
		free(block);
		return o;
	}
	free(block);
	return Py_BuildValue("issy", ret, "", "", 0);
}


static PyObject* mnfc_write(PyObject* self, PyObject* args)
{
	int ret = 0;
	
	int blockNum;
	const char* uid;
	const char* data;
	Py_ssize_t data_len;
	PyArg_ParseTuple(args, "isy#", &blockNum, &uid, &data, &data_len);
	
	if(data_len < sizeof(MifareClassicBlock)*3)
	{
		printf("NFC: invalid write block len\n");
		return Py_BuildValue("i", -1);
	}

	const MifareClassicBlock* block = (MifareClassicBlock*)data;
	
Py_BEGIN_ALLOW_THREADS

	MifareTag* tags = freefare_get_tags(device);
	if(!tags)
	{
		printf("NFC: device error while listing tags\n");
		ret = 1;
		goto error;
	}

	if(tags[0])
	{
		char* tag_uid = freefare_get_tag_uid(tags[0]);
		if(strncmp(tag_uid, uid, MAX_UID_LEN) != 0)
		{
			printf("NFC: tag %s not found for write operation\n", uid);
			ret = 2;
		}
		free(tag_uid);
		
		if(!ret)
		{
			if(mifare_classic_connect(tags[0]))
			{
				printf("NFC: mifare_classic_connect failed\n");
				ret = 3;
				goto error;
			}

			MifareClassicBlockNumber b = blockNum*4;
			if(mifare_classic_authenticate(tags[0], b, default_keys[0], MFC_KEY_B))
			{
				printf("NFC: auth failed\n");
				ret = 4;
				goto error;
			}

			for(int k = 0; k < 3; k++)
			{
				int n = mifare_classic_write(tags[0], b+k, block[k]);
				if(n < 0)
				{
					printf("NFC: write error\n");
					ret = 5;
					goto error;
				}
			}
		}
	}
	else
	{
		ret = 6;
	}

error:
	freefare_free_tags(tags);
	
Py_END_ALLOW_THREADS

	return Py_BuildValue("i", ret);
}

static PyMethodDef module_methods[] = {
	{"init", &mnfc_init, METH_VARARGS, "initialize nfc backend"},
	{"deinit", &mnfc_deinit, METH_VARARGS, "deinitialize nfc backend"},
	{"read", &mnfc_read, METH_VARARGS, "read data from tag"},
	{"write", &mnfc_write, METH_VARARGS, "write data to tag"},
	{NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC PyInit_mnfc(void)
{
	PyObject* module;
	static struct PyModuleDef moduledef = {
		PyModuleDef_HEAD_INIT,
		"mnfc",
		"basic NFC communication",
		-1,
		module_methods,
		NULL,
		NULL,
		NULL,
		NULL
	};
	module = PyModule_Create(&moduledef);
	if(!module)
		return NULL;
	
	return module;
}

