#!/usr/bin/python3
#
#	Mifare NFC Python Module for Heiko
#	Copyright (C) 2019  Christian Carlowitz <chca@cmesh.de>
#
#	This program is free software: you can redistribute it and/or modify it
#	under the terms of the GNU Lesser General Public License as published by the
#	Free Software Foundation, either version 3 of the License, or (at your
#	option) any later version.
#
#	This program is distributed in the hope that it will be useful, but WITHOUT
#	ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
#	FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License
#	for more details.
#
#	You should have received a copy of the GNU Lesser General Public License
#	along with this program.  If not, see <http://www.gnu.org/licenses/>
#

import sys
import mnfc
import time

if len(sys.argv) < 2:
	print("usage: mnfc_test MODE")
	sys.exit(1)
mode = sys.argv[1]

mnfc.init()

if mode == "s":
	try:
		while True:
			v,uid,ttype,dat = mnfc.read(1,15)
			if v == 0:
				print("uid:", uid)
				print("type:", ttype)

				for i in range(0,len(dat)):
					if i % 16 == 0:
						print()
					print("%02x " % dat[i], end='')
				print()
			else:
				print("no tag")
				
			time.sleep(1)

	except KeyboardInterrupt:
		print("\nexiting ...")
		mnfc.deinit()

elif mode == "w":
	dat = bytes(range(0,16*3))*15
	mnfc.write(1, 15, "7b3a6f1f", dat)


