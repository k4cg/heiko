import sqlite3
import getpass
import swagger_client
from heiko.utils import log
from string import ascii_letters

def migrate_user(auth, client):
    """
    Migration function that reads data from old matomat sqlite and creates user in the backend

    :auth: dict
    :returns: bool
    """

    sq = sqlite3.connect('/tmp/matomat.db')

    log("Please give username to look for in sqlite from matomat.db")
    name = input("Username: ")

    if len(name) < 3:
        log("Username too short (>=3).", serv="Error")
        return False

    if not all(c in ascii_letters+'-' for c in name):
        log("Username not valid. Please be alphanumerical.", serv="Error")
        return False

    log("Looking for user %s in matomat.db..." % name)
    cur = sq.cursor()
    cur.execute("SELECT username, credits from user where username = \"%s\";" % name)
    rows = cur.fetchall()

    if len(rows) > 1:
        log("Search resulted in multiple result sets... exitting", serv="ERROR")
        return False

    user_to_migrate, credits_to_migrate = rows[0]

    if float(credits_to_migrate) < 0:
        log("User has negative credits and this is currently not supported by backend. Hold on until https://github.com/k4cg/matomat-service/issues/7 is fixed")
        return False

    log("Found user %s with credits %.2f Euro!" % (user_to_migrate, int(credits_to_migrate) / 100), serv="SUCCESS")

    confirmation = input("Wanna migrate her? (y/n): ").lower()[0]
    if confirmation != 'y':
        log("Aborting...")
        return False

    admin = input("Wanna make her admin? (y/n): ").lower()[0]

    if admin is 'n':
        admin = 1
    else:
        admin = 0

    log("Please add new credentials!")
    password = getpass.getpass("Password: ")
    passwordrepeat = getpass.getpass("Repeat password: ")

    # Creating user
    try:
        new_user = client.users_post(user_to_migrate, password, passwordrepeat, admin)
        log("Successfully created user %s" % user_to_migrate, serv="SUCCESS")
        return True
    except:
        log("Error creating user", serv="ERROR")
        return False

    # Adding credits
    try:
        users = client.users_user_id_credits_add_patch(new_user.to_dict()["id"], credits_to_migrate)
        log("Set credit to %s" % credits_to_migrate, serv="SUCCESS")
        return True
    except:
        log("Error adding credits %s" % credits_to_migrate, serv="ERROR")
        return False
