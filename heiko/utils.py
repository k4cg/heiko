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


def yes_or_no(question):
    """
    Ask the user a question that can be answered with yes or no.

    :question: str, The question
    :returns: bool, True if the answer was yes, False otherwise
    """
    answer = input("{} (y/n): ".format(question)).lower()
    if answer == "y":
        return True
    return False
