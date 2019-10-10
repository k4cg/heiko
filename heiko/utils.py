from sty import fg


def log(msg, serv="INFO"):
    """
    Interface to print informations to the user.

    :msg: str
    :serv: [ INFO, ERROR, SUCCESS ]
    :returns: bool
    """
    if serv.upper() == "ERROR":
        msg = fg.red + "Error: " + msg + fg.rs
    elif serv.upper() == "SUCCESS":
        msg = fg.green + msg + fg.rs

    print(msg)

    return True
