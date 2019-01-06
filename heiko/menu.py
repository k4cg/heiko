import os
from string import ascii_letters
from sty import fg

import swagger_client
from heiko.items import list_items, consume_item, create_item
from heiko.users import add_credits, list_users, create_user
from heiko.utils import log

### User Menu Mapping

# Menu Mapping
KEY_LIST_ITEMS = 1
KEY_CONSUME_MATE = 2
KEY_CONSUME_BEER = 3
KEY_LIST_USERS = 4
KEY_INSERT_COINS = 5
KEY_CREATE_USER = 6
KEY_CREATE_ITEM = 7
KEY_HELP = 8
KEY_EXIT = 9

actions = {
    KEY_LIST_ITEMS: "Show drinks",
    KEY_CONSUME_MATE: "Consume Mate",
    KEY_CONSUME_BEER: "Consume Beer",
    KEY_LIST_USERS: "Show users",
    KEY_INSERT_COINS: "Insert coins",
    KEY_CREATE_USER: "Create user",
    KEY_CREATE_ITEM: "Create drink",
    KEY_HELP: "Help",
    KEY_EXIT: "Exit",
}

def user_menu(auth, items_client, users_client):
    """
    Shows the menu to the user, clears screen, draws the navigation screen
    This is kind of the main loop of heiko. If you need new options, add them here
    otherwise they are not being executed.

    :auth: dict
    :returns: is_logged_in, is_exit (both bool)
    """


    try:
        option = int(input(">>> "))
    except ValueError:
        os.system('clear')
        banner(auth)
        option = KEY_HELP

    if option == KEY_LIST_ITEMS:
        list_items(auth, items_client)
    if option == KEY_CONSUME_MATE:
        consume_item(auth, items_client, 1)
    if option == KEY_CONSUME_BEER:
        consume_item(auth, items_client, 2)
    if option == KEY_INSERT_COINS:
        add_credits(auth, users_client)
    if option == KEY_HELP:
        help(auth)

    # Admin options
    if auth["user"]["admin"] is True:
        if option == KEY_LIST_USERS:
            list_users(auth, users_client)

        if option == KEY_CREATE_USER:
            create_user(auth, users_client)

        if option == KEY_CREATE_ITEM:
            create_item(auth, items_client)

    if option == KEY_EXIT:
        return False, True

    return True, False


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
            log("Hi %s, current credits: %.2f. You are admin!\n" % (auth["user"]["username"], auth["user"]["credits"] / 100))
        else:
            log("Hi %s, current credits: %.2f\n." % (auth["user"]["username"], auth["user"]["credits"] / 100))

    return True


def help(auth):
    """
    Shows the basic navigation to the user.

    :auth: dict
    :returns: bool
    """

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

    # user = input('User: ')
    # password = getpass.getpass('Password: ')
    user = "admin"
    password = "admin"

    token = None
    is_logged_in = False

    try:
        auth = auth_client.auth_login_post(user, password).to_dict()
        is_logged_in = True
    except swagger_client.rest.ApiException:
        log("Wrong username and/or password!",serv="ERROR")
        time.sleep(1)

    return is_logged_in, auth

