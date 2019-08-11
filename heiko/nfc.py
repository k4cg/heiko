
import getpass
from heiko.utils import log
from nfc import mnfc

def nfc_init():
    mnfc.init()

def nfc_read():
    v,uid,ttype,dat = mnfc.read(1,1)
    if v == 0:
        log("found " + ttype + " with uid " + uid)
        return uid

def nfc_write(uid, token):
    datLen = 15*3*16
    b = token.encode()
    b += b"\x00"*(datLen-len(b))
    v = mnfc.write(1,15,uid,b)
    if v == 0:
        log("write successful")
