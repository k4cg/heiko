import sqlite3
import getpass
from heiko.utils import log


def migrate_user(auth, client):
    """
    Migration function that reads data from old matomat sqlite and creates user in the backend

    :auth: dict
    :returns: bool
    """

    sq = sqlite3.connect('/home/heiko/matomat.db')

    log("Please give username to look for in sqlite from matomat.db")
    name = input("Username: ")

    if len(name) < 3:
        log("Username too short (>=3).", serv="Error")
        return False

    if name.isalnum() is False:
        log("Username not valid. Please be alphanumerical.", serv="Error")
        return False

    log("Looking for user %s in matomat.db..." % name)

    # fetch results from sqlite
    cur = sq.cursor()
    cur.execute("SELECT username, credits from user where username = \"%s\";" % name)
    rows = cur.fetchall()

    # closing sqlite connection
    sq.commit()
    sq.close()

    if len(rows) > 1:
        log("Search resulted in multiple result sets... exitting", serv="ERROR")
        return False

    # assign values
    user_to_migrate, credits_to_migrate = rows[0]

    log("Found user %s with credits %.2f Euro!" % (user_to_migrate, int(credits_to_migrate) / 100), serv="SUCCESS")

    confirmation = input("Wanna migrate her? (y/n): ").lower()[0]
    if confirmation != 'y':
        log("Aborting...")
        return False

    admin = input("Wanna make her admin? (y/n): ").lower()[0]

    if admin is 'y':
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
    except:
        log("Error creating user", serv="ERROR")
        return False

    # Adding credits

    if float(credits_to_migrate) < 0:
        wi = str(int(credits_to_migrate)).replace('-', '')
        try:
            client.users_user_id_credits_withdraw_patch(new_user.to_dict()["id"], int(wi))
            log("Set credit to %.2f" % (float(credits_to_migrate) / 100), serv="SUCCESS")
        except:
            log("Error setting credits to %.2f" % (float(credits_to_migrate) / 100), serv="ERROR")
            return False

    else:
        try:
            client.users_user_id_credits_add_patch(new_user.to_dict()["id"], int(credits_to_migrate))
            log("Set credit to %.2f" % (float(credits_to_migrate) / 100), serv="SUCCESS")
        except:
            log("Error setting credits to %.2f" % (float(credits_to_migrate) / 100), serv="ERROR")
            return False

    return True
