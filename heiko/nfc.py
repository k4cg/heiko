from heiko.utils import log

def nfc_init():
    global mnfc
    from nfc import mnfc
    mnfc.init()

def nfc_detect():
    key = bytes([0xff,0xff,0xff,0xff,0xff,0xff])
    v,uid,ttype,dat = mnfc.read(1,1,key,False)
    if v == 0:
        log("found " + ttype + " with uid " + uid)
        return uid

def nfc_read(uid):
    key = bytes([0xff,0xff,0xff,0xff,0xff,0xff])
    v,ruid,ttype,dat = mnfc.read(1,15,key,False)
    if ruid == uid:
        return dat.decode().strip("\x00")

def nfc_write(uid, token):
    key = bytes([0xff,0xff,0xff,0xff,0xff,0xff])
    datLen = 15*3*16
    b = token.encode()
    b += b"\x00"*(datLen-len(b))
    v = mnfc.write(1,15,uid,b,key,False)
    if v == 0:
        log("write successful")
