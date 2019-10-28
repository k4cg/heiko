from heiko.utils import log
import swagger_client
import urllib3


DEFAULT_KEY = bytes([0xff, 0xff, 0xff, 0xff, 0xff, 0xff])


def nfc_init():
    global mnfc
    from nfc import mnfc
    mnfc.init()


def nfc_detect():
    key = DEFAULT_KEY.copy()
    v, uid, ttype, dat = mnfc.read(1, 1, key, False)
    header = ""
    try:
        header = dat.decode()
    except:
        pass
    if v == 0:
        log("found " + ttype + " with uid " + uid)
        return uid, header
    return None, None


def nfc_read(uid, key=None):
    if key is None:
        key = DEFAULT_KEY.copy()
    v, ruid, ttype, dat = mnfc.read(2, 14, key, False)
    if ruid == uid:
        return dat.decode().strip("\x00")


def nfc_write(uid, header, token, key=None):
    if key is None:
        key = DEFAULT_KEY.copy()

    secLen = 3 * 16
    hb = header.encode()
    hb += b"\x00" * (secLen - len(hb))

    datLen = 14 * secLen
    b = token.encode()
    b += b"\x00" * (datLen - len(b))

    v = mnfc.write(1, 15, uid, hb + b, key, False)
    if v == 0:
        log("write successful")


def nfc_format_card(auth_client, username, password):
    uid, header = nfc_detect()
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
                validityseconds=days * 3600 * 24).to_dict()
            token = auth2["token"]
        except swagger_client.rest.ApiException:
            log("Wrong password!", serv="ERROR")
            return False
        except (ConnectionRefusedError, urllib3.exceptions.MaxRetryError):
            log("Connection to backend was refused!", serv="ERROR")
            return False
        nfc_write(uid, "matomat1:" + username + ":", token)
        return True
    return False
