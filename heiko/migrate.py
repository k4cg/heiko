import sqlite3
import getpass
from heiko.utils import log, yes_or_no
import os


def migrate_user(auth, client, cfgobj):
    """
    Migration function that reads data from old matomat sqlite and creates user in the backend

    :auth: dict
    :client: userauth object
    :cfgobj: config dict
    :returns: bool
    """

    # Check if configured database is there and can be read
    try:
        migration_database = cfgobj["accounting"]["migration_database"]
        if os.access(migration_database, os.R_OK):
            matomat_db = sqlite3.connect(migration_database)
        else:
            raise IOError
    except (IOError, KeyError):
        log("Migration database cannot be found or is not configured. Aborting.", serv="ERROR")
        return False

    # First, ask for Admin yes/no
    is_admin = yes_or_no("Should the migrated user be admin?")
    if is_admin:
        admin = 1
    else:
        admin = 0

    # Search Username
    log("Please give username to look for in sqlite from matomat.db")
    name = input("Username: ")

    if len(name) < 3:
        log("Username too short (>=3).", serv="Error")
        return False

    if name.isalnum() is False:
        log("Username not valid. Please be alphanumerical.", serv="Error")
        return False

    log("Looking for user %s in given sqlite..." % name)

    # fetch results from sqlite
    cur = matomat_db.cursor()
    cur.execute("SELECT username, credits from user where username = \"%s\";" % name)
    rows = cur.fetchall()
    matomat_db.commit()
    matomat_db.close()

    if len(rows) > 1:
        log("Search resulted in multiple result sets... exitting", serv="ERROR")
        return False

    # assign values
    user_to_migrate, credits_to_migrate = rows[0]

    log("Found user {} with credits {:.2f} Euro!".format(user_to_migrate, int(credits_to_migrate) / 100), serv="SUCCESS")

    confirmation = yes_or_no("Wanna migrate her?")
    if confirmation is False:
        log("Aborting...")
        return False

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

    try:
        if float(credits_to_migrate) < 0:
            credits_to_migrate = str(int(credits_to_migrate)).replace('-', '')
            client.users_user_id_credits_withdraw_patch(new_user.to_dict()["id"], int(credits_to_migrate))
            log("Set credit to -{:.2f}".format(float(credits_to_migrate) / 100), serv="SUCCESS")
        else:
            client.users_user_id_credits_add_patch(new_user.to_dict()["id"], int(credits_to_migrate))
            log("Set credit to {:.2f}".format(float(credits_to_migrate) / 100), serv="SUCCESS")
    except:
        log("Error setting credits {:.2f}".format(float(credits_to_migrate) / 100), serv="ERROR")
        return False

    return True
