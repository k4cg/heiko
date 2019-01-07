import time
import getpass
import os
from sty import fg

import swagger_client
from heiko.items import list_items, consume_item, create_item, delete_item
from heiko.users import add_credits, list_users, create_user, reset_user_password, delete_user
from heiko.utils import log
from heiko.migrate import migrate_user


### User Menu Mapping
USER_KEY_CONSUME_MATE = 1
USER_KEY_CONSUME_BEER = 2
USER_KEY_CONSUME_SCHORLE = 3 #TODO
USER_KEY_CONSUME_COLA = 4 #TODO
USER_KEY_INSERT_COINS = 5
USER_KEY_SHOW_STATS = 6 # TODO
USER_KEY_ADMINISTRATION = 7 #TODO
USER_KEY_EXIT = 9
USER_KEY_HELP = "?"

user_actions = {
    USER_KEY_CONSUME_MATE: "Consume Club Mate",
    USER_KEY_CONSUME_BEER: "Consume Bier",
    USER_KEY_CONSUME_SCHORLE: "Consume Apfelschorle",
    USER_KEY_CONSUME_COLA: "Consume Mate Cola",
    USER_KEY_INSERT_COINS: "Insert coins",
    USER_KEY_ADMINISTRATION: "Administration",
    USER_KEY_EXIT: "Exit",
    USER_KEY_HELP: "Help",
}

### Admin Menu Mapping
ADMIN_KEY_LIST_ITEMS = 1
ADMIN_KEY_LIST_USERS = 2
ADMIN_KEY_CREATE_USER = 3
ADMIN_KEY_CREATE_ITEM = 4
ADMIN_KEY_DELETE_ITEM = 5
ADMIN_KEY_RESET_USER_PASSWORD = 6
ADMIN_KEY_MIGRATE_USER = 7
ADMIN_KEY_DELETE_USER = 8
ADMIN_KEY_RESET_CREDITS = 9
ADMIN_KEY_EXIT = 10
ADMIN_KEY_HELP = "?"

admin_actions = {
    ADMIN_KEY_LIST_ITEMS: "Show drinks",
    ADMIN_KEY_LIST_USERS: "Show users",
    ADMIN_KEY_CREATE_USER: "Create user",
    ADMIN_KEY_CREATE_ITEM: "Create drink",
    ADMIN_KEY_DELETE_ITEM: "Delete drink",
    ADMIN_KEY_RESET_USER_PASSWORD: "Reset password for user",
    ADMIN_KEY_MIGRATE_USER: "Migrate user from old Matomat",
    ADMIN_KEY_DELETE_USER: "Delete user",
    ADMIN_KEY_RESET_CREDITS: "Reset credits from user",
    ADMIN_KEY_EXIT: "Exit",
    ADMIN_KEY_HELP: "Help",
}

### Functions

def user_menu(auth, items_client, users_client):
    """
    Shows the menu to the user, clears screen, draws the navigation screen
    This is kind of the main loop of heiko. If you need new options, add them here
    otherwise they are not being executed.

    :auth: dict
    :items_client: object
    :users_client: object
    :returns: is_logged_in, is_exit (both bool)
    """


    try:
        option = int(input(">>> "))
    except ValueError:
        os.system('clear')
        banner(auth)
        option = USER_KEY_HELP

    if option == USER_KEY_CONSUME_MATE:
        consume_item(auth, items_client, 1)

    if option == USER_KEY_CONSUME_BEER:
        consume_item(auth, items_client, 2)

    if option == USER_KEY_CONSUME_SCHORLE:
        consume_item(auth, items_client, 3)

    if option == USER_KEY_CONSUME_SCHORLE:
        consume_item(auth, items_client, 4)

    if option == USER_KEY_INSERT_COINS:
        add_credits(auth, users_client)

    if option == USER_KEY_SHOW_STATS:
        log("Not implemented yet", serv="ERROR")

    if option == USER_KEY_ADMINISTRATION:
        is_exit = False
        while is_exit is False:
            is_exit = admin_menu(auth, items_client, users_client)

    if option == USER_KEY_HELP:
        show_help(auth, admin=False)

    if option == USER_KEY_EXIT:
        return False, True

    return True, False


def admin_menu(auth, items_client, users_client):
    """
    Shows the menu to the admin, clears screen, draws the navigation screen

    :auth: dict
    :returns: is_logged_in, is_exit (both bool)
    """

    if auth["user"]["admin"] is False:
        log("Meeeep. Not an administrator, but nice try.", serv="ERROR")
        log("Computer says no.", serv="ERROR")
        return True # is_exit

    try:
        option = int(input(">>> "))
    except ValueError:
        os.system('clear')
        banner(auth)
        option = ADMIN_KEY_HELP

    if option == ADMIN_KEY_LIST_ITEMS:
        list_items(auth, items_client)

    if option == ADMIN_KEY_LIST_USERS:
        list_users(auth, users_client)

    if option == ADMIN_KEY_CREATE_USER:
        create_user(auth, users_client)

    if option == ADMIN_KEY_CREATE_ITEM:
        create_item(auth, items_client)

    if option == ADMIN_KEY_DELETE_ITEM:
        delete_item(auth, items_client)

    if option == ADMIN_KEY_RESET_USER_PASSWORD:
        reset_user_password(auth, users_client)

    if option == ADMIN_KEY_MIGRATE_USER:
        migrate_user(auth, users_client)

    if option == ADMIN_KEY_DELETE_USER:
        delete_user(auth, users_client)

    if option == ADMIN_KEY_RESET_CREDITS:
        reset_credits(auth, users_client)

    if option == ADMIN_KEY_HELP:
        show_help(auth, admin=True)

    if option == ADMIN_KEY_EXIT:
        log("Switching back to normal menu, sir.", serv="SUCCESS")
        return True

    return False


def banner(auth=None):
    """
    Prints a fancy ascii art banner to user and (if already logged in)
    greets the person with username and current credits

    :auth: dict
    :returns: bool
    """

    mate_banner = """
 __  __    _  _____ ___  __  __    _  _____
|  \/  |  / \|_   _/ _ \|  \/  |  / \|_   _|
| |\/| | / _ \ | || | | | |\/| | / _ \ | |
| |  | |/ ___ \| || |_| | |  | |/ ___ \| |
|_|  |_/_/   \_\_| \___/|_|  |_/_/   \_\_|
"""
    log(mate_banner)
    if auth is not None:
        if auth["user"]["admin"] is True:
            log("Hi %s, current credits: %.2f Euro. You are admin!\n" % (auth["user"]["username"], auth["user"]["credits"] / 100))
        else:
            log("Hi %s, current credits: %.2f Euro\n." % (auth["user"]["username"], auth["user"]["credits"] / 100))

    return True


def show_help(auth, admin=False):
    """
    Shows the basic navigation to the user.

    :auth: dict
    :returns: bool
    """

    if admin is True:
        actions = admin_actions
    else:
        actions = user_actions

    log("Available actions:")
    for key in actions.keys():
        log("[%s] %s" % (key, actions[key]))

    return True


def login(maas_builder):
    """
    Shows banner, asks user to authenticate via username/password
    and creates auth token that we reuse after auth was successful once.

    :returns: tuple
    """
    auth_client = maas_builder.build_auth_api_client()

    os.system('clear')
    banner()
    log("Please authenticate yourself!")

    user = input('User: ')
    password = getpass.getpass('Password: ')
    # user = "admin"
    # password = "admin"
    # user = "noqqe"
    # password = "flo"

    token = None
    is_logged_in = False
    auth = None

    try:
        auth = auth_client.auth_login_post(user, password).to_dict()
        is_logged_in = True
    except swagger_client.rest.ApiException:
        log("Wrong username and/or password!",serv="ERROR")
        time.sleep(1)

    return is_logged_in, auth

