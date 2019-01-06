import json
import time
import getpass
import swagger_client
from heiko.utils import log
from string import ascii_letters

def list_users(auth, client):
    """
    Shows all users from the database to an successfully authenticated administrator

    :auth: dict
    :returns: bool
    """

    try:
        users = client.users_get()
    except swagger_client.rest.ApiException:
        log("Could fetch users from the database.",serv="ERROR")
        return False

    log("List of current users in the database:\n")
    log("ID\tCredits\tUsername")
    for user in users:
        user = user.to_dict()
        log("%s\t%s\t%s" % (user["id"], user["credits"], user["username"]))

    return True

def create_user(auth, client):
    """
    Asks administrator for details and
    creates a new user in the database.

    :auth: dict
    :returns: bool
    """


    name = input("Username: ")

    if not all(c in ascii_letters+'-' for c in name):
        log("Username not valid. Please be alphanumerical.", serv="Error")
        return False

    admin = input("Admin? (y/n): ").lower()[0]

    if admin is 'y':
        admin = 1

    password = getpass.getpass("Password: ")
    passwordrepeat = getpass.getpass("Repeat password: ")

    try:
        users = client.users_post(name, password, passwordrepeat, admin)
        return True
    except:
        log("Error creating user", serv="ERROR")
        return False


### UserApi Functions for Users

def add_credits(auth, client):
    """
    Asks user to input the amount he put into the box and adds this amount of credits to his/her account

    :auth: dict
    :returns: bool
    """

    try:
        credits = float(input("EUR: "))
        if credits < 0 or credits > 100:
            raise ValueError
    except ValueError:
        log("Invalid input. Valid values: 1-100",serv="ERROR")
        return False

    # calc input from eur into cents
    cents = float(credits) * 100

    try:
        # send update request to backend
        client.users_user_id_credits_add_patch(str(auth["user"]["id"]), cents)

        # TODO: Replace hack that updates local auth object to reflect changes into the banner
        auth["user"]["credits"] = auth["user"]["credits"] + cents

        #notify user
        log("Your credit is now %.2f" % (auth["user"]["credits"] / 100), serv="SUCCESS")
        return True
    except:
        log("Updating your credits in the backend was not successful. Ask people for help",serv="ERROR")
        return False


