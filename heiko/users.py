import getpass
import random
import string
from tabulate import tabulate
import swagger_client

from heiko.utils import log, yes_or_no
from heiko.nfc import nfc_format_card


def find_user_by_username(auth, client):
    """
    Helper function that returns a user object that is found
    by searching for a username

    :auth: dict
    :client: users_client object
    :username: str
    :returns: user object
    """

    user_to_find = None
    user_object = None

    user_to_find = input("Username: ")

    if len(user_to_find) < 3 or user_to_find is None:
        log("Username too short (>=3).", serv="Error")
        return False

    # find user id
    users = client.users_get()
    for user in users:
        if user.to_dict()["username"] == user_to_find:
            user_object = user.to_dict()

    if user_object is None:
        log("Could not find user %s. Are you sure about the username?" % user_to_find, serv="ERROR")
        return False

    return user_object


def list_users(auth, client):
    """
    Shows all users from the database to an successfully authenticated administrator

    :auth: dict
    :returns: bool
    """

    try:
        users = client.users_get()
    except swagger_client.rest.ApiException:
        log("Could fetch users from the database.", serv="ERROR")
        return False

    it = []
    for u in users:
        d = u.to_dict()
        it.append([d["id"], d["username"], float(d["credits"]) / 100, d["admin"]])

    log("List of current users in the database:\n")
    log(tabulate(it, headers=["ID", "Username", "Credits (EUR)", "Admin?"], tablefmt="presto", floatfmt=".2f"))

    return True


def show_user_stats(auth, client):
    """
    Presents consumption statistics to user

    :auth: dict
    :client: users_client object
    :returns: bool
    """

    try:
        stats = client.users_user_id_stats_get(auth["user"]["id"])
    except swagger_client.rest.ApiException:
        log("Could fetch stats from the database.", serv="ERROR")
        return False

    drinks = []
    sum_money = 0
    for drink in stats:
        money = float(drink["consumed"]) * float(drink["cost"]) / 100
        sum_money = sum_money + money
        drinks.append([drink["name"], drink["consumed"], money])

    log("Your consumption statistics:\n")
    log(tabulate(drinks, headers=["Name", "Consumptions", "Coins spent (EUR)"], tablefmt="presto", floatfmt=".2f"))

    log("\nCoins spent overall: {:.2f} EUR".format(sum_money))
    return True


def create_user(auth, client):
    """
    Asks administrator for details and
    creates a new user in the database.

    :auth: dict
    :returns: bool
    """

    is_admin = yes_or_no("Admin?")

    if is_admin:
        admin = 1
    else:
        admin = 0

    name = input("Username: ")

    if len(name) < 3:
        log("Username too short (>=3).", serv="Error")
        return False

    if name.isalnum() is False:
        log("Username not valid. Please be alphanumerical.", serv="Error")
        return False

    password = getpass.getpass("Password: ")
    passwordrepeat = getpass.getpass("Repeat password: ")

    try:
        client.users_post(name, password, passwordrepeat, admin)
        return True
    except:
        log("Error creating user", serv="ERROR")
        return False


def transfer_coins(auth, client):
    """
    Transfer credits to another user

    :auth_client: dict
    :user_client: dict
    :returns: bool
    """

    log("What user you want to send credits to?")
    target_user = find_user_by_username(auth, client)

    if target_user is False:
        # error message already printed at this point by find_user_by_username()
        return False

    # Ask for amount to transfer
    try:
        credits_to_transfer = float(input("How many credits you want to transfer (i.e. 1 or 1.20): ")) * 100
    except ValueError:
        return False

    try:
        req = client.users_user_id_credits_transfer_patch(user_id=target_user['id'], credits=int(credits_to_transfer))
        transferred_credits = float(req.to_dict()['credits']) / 100
        log("Successfully transferred {:.2f} credits to user {}".format(transferred_credits, target_user['username']), serv="SUCCESS")
        return True
    except:
        log("Error transferring credits to user {}".format(target_user['username']), serv="ERROR")
        return False


def create_user_nfc(auth_client, user_client):
    """
    Asks administrator for details and
    creates a new NFC user in the database
    (= user with random dummy password and NFC token).

    :auth: dict
    :returns: bool
    """

    name = input("Username: ")

    if len(name) < 3:
        log("Username too short (>=3).", serv="Error")
        return False

    if name.isalnum() is False:
        log("Username not valid. Please be alphanumerical.", serv="Error")
        return False

    is_admin = yes_or_no("Admin?")

    if is_admin:
        admin = 1
    else:
        admin = 0

    password = "".join(random.choice(string.ascii_letters + "0123456789") for i in range(23))

    try:
        user_client.users_post(name, password, password, admin)
    except:
        log("Error creating user", serv="ERROR")
        return False

    return nfc_format_card(auth_client, name, password)


def delete_user(auth, client):
    """
    Delete a user

    :auth: dict
    :client: users_client object
    """

    log("What user you want to delete?")

    user_to_delete = find_user_by_username(auth, client)
    if user_to_delete is False:
        log("Could not find user.", serv="ERROR")
        return False

    confirmation = yes_or_no("You really want to delete %s?" % user_to_delete["username"])

    if confirmation is False:
        log("Aborted...")
        return False

    try:
        client.users_user_id_delete(int(user_to_delete["id"]))
        log("Successfully deleted user %s" % user_to_delete["username"], serv="SUCCESS")
        return True
    except:
        log("Could not delete user %s. Error by backend" % user_to_delete["username"], serv="ERROR")
        return False


def reset_credits(auth, client):
    """
    Set credits to defined amount by admin

    :auth: dict
    :client: users_client object
    :returns: bool
    """
    log("What user you want to set the credits for?")
    user_to_reset = find_user_by_username(auth, client)
    if user_to_reset is False:
        log("Could not find user.", serv="ERROR")
        return False

    new_credits = float(input("Set new credits (EUR): ")) * 100

    try:
        client.users_user_id_credits_withdraw_patch(user_to_reset["id"], user_to_reset["credits"])
        r = client.users_user_id_credits_add_patch(user_to_reset["id"], int(new_credits))
        auth["user"]["credits"] = r.to_dict()["credits"]
        log("Successfully set the credits for user %s to %.2f Euro" % (user_to_reset["username"], new_credits / 100), serv="SUCCESS")
        return True
    except:
        log("Could not set the credits for user %s to %.2f Euro. Backend error." % (user_to_reset["username"], new_credits), serv="ERROR")
        return False


def add_credits_admin(auth, client):
    """
    Add credits by admin

    :auth: dict
    :client: users_client object
    :returns: bool
    """
    log("What user you want to add the credits for?")
    user = find_user_by_username(auth, client)
    if user is False:
        log("Could not find user.", serv="ERROR")
        return False

    add_credits = float(input("Paid amount (EUR): ")) * 100

    try:
        r = client.users_user_id_credits_add_patch(user["id"], int(add_credits))
        auth["user"]["credits"] = r.to_dict()["credits"]
        log("Successfully set the credits for user %s to %.2f Euro" % (user["username"], auth["user"]["credits"] / 100), serv="SUCCESS")
        return True
    except:
        log("Could not add %.2f Euro credits for user %s. Backend error." % (add_credits, user["username"]), serv="ERROR")
        return False


def reset_user_password(auth, client):
    """
    Gives an admin the capability to reset password for a specific user.
    It asks for username, trys to find userid by name and then asks for new password.

    :auth: dict
    :client: users_client object
    :returns: bool
    """
    log("What user you want to reset the password for?")
    user_to_reset = find_user_by_username(auth, client)

    if user_to_reset is False:
        log("Could not find user.", serv="ERROR")
        return False

    passwordnew = getpass.getpass("Password: ")
    passwordrepeat = getpass.getpass("Repeat password: ")

    try:
        client.users_user_id_resetpassword_patch(user_to_reset["id"], passwordnew, passwordrepeat)
        log("Successfully changed password for user %s with id %s." % (user_to_reset["username"], user_to_reset["id"]), serv="SUCCESS")
        return True
    except:
        log("Could not reset password for user %s with id %s. Error by backend" % (user_to_reset["username"], user_to_reset["id"]), serv="ERROR")
        return False


def reset_user_nfc(auth, auth_client, user_client):
    """
    Gives an admin the capability to reset password for a specific user and write new nfc token.
    It asks for username, trys to find userid by name and then asks for new password.

    :auth: dict
    :client: users_client object
    :returns: bool
    """
    log("What user you want to reset the password for?")
    user_to_reset = find_user_by_username(auth, user_client)

    if user_to_reset is False:
        log("Could not find user.", serv="ERROR")
        return False

    password = "".join(random.choice(string.ascii_letters + "0123456789") for i in range(23))

    try:
        user_client.users_user_id_resetpassword_patch(user_to_reset["id"], password, password)
        log("Successfully reset password for user %s with id %s." % (user_to_reset["username"], user_to_reset["id"]), serv="SUCCESS")
    except:
        log("Could not reset password for user %s with id %s. Error by backend" % (user_to_reset["username"], user_to_reset["id"]), serv="ERROR")
        return False

    return nfc_format_card(auth_client, user_to_reset["username"], password)


def change_password(auth, client):
    """
    Gives user the capability to reset password for himself/herself.

    :auth: dict
    :client: users_client object
    :returns: bool
    """

    password = getpass.getpass("Current Password: ")
    passwordnew = getpass.getpass("New Password: ")
    passwordrepeat = getpass.getpass("Repeat password: ")

    try:
        client.users_user_id_password_patch(auth["user"]["id"], password, passwordnew, passwordrepeat)
        log("Successfully changed your password!", serv="SUCCESS")
        return True
    except:
        log("Could not set your password. Error by backend", serv="ERROR")
        return False

# UserApi Functions for Users


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
        log("Invalid input. Valid values: 1-100", serv="ERROR")
        return False

    # calc input from eur into cents
    cents = credits * 100

    try:
        # send update request to backend
        r = client.users_user_id_credits_add_patch(str(auth["user"]["id"]), int(cents))

        # TODO: Replace hack that updates local auth object to reflect changes into the banner
        auth["user"]["credits"] = r.to_dict()["credits"]

        # notify user
        log("Your credit is now %.2f" % (auth["user"]["credits"] / 100), serv="SUCCESS")
        return True
    except:
        log("Updating your credits in the backend was not successful. Ask people for help", serv="ERROR")
        return False
