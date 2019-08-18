from heiko.utils import log
from datetime import datetime, timedelta


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
        
def nfc_format_card(auth_client, username, password):
    uid = nfc_detect()
    if uid is not None:
        ans = input("overwrite card? [yN] ")
        if ans != "y":
            return False
        ans = input("token lifetime in days? ")
        if not ans.isnumeric():
            log("invalid lifetime")
            return False
        days = int(ans)
        token = ""
        try:
            auth2 = auth_client.auth_login_post(
                username, password,
                validityseconds=days*3600*24).to_dict()
            token = auth2["token"]
        except swagger_client.rest.ApiException:
            log("Wrong password!",serv="ERROR")
            return False
        except (ConnectionRefusedError, urllib3.exceptions.MaxRetryError):
            log("Connection to backend was refused!",serv="ERROR")
            return False
        validstamp = (datetime.now()+timedelta(days=days)).timestamp()
        nfc_write(uid, token)
        return True
    return False


