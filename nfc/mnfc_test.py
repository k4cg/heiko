#!/usr/bin/python3

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
			v,uid,ttype,dat = mnfc.read(1)
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
	dat = bytes(range(0,48))
	block = 1
	mnfc.write(block, "7b3a6f1f", dat)


