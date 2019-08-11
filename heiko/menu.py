import time
import getpass
import os
import urllib3

import swagger_client
from heiko.items import list_items, consume_item, create_item, delete_item
from heiko.users import add_credits, list_users, create_user, reset_user_password, delete_user, reset_credits, change_password, show_user_stats
from heiko.service import show_service_stats
from heiko.utils import log
from heiko.voice import say, greet_user
from heiko.migrate import migrate_user
from heiko.nfc import nfc_read, nfc_write

from datetime import datetime, timedelta

### User Menu Mapping
USER_KEY_CONSUME_MATE = 1
USER_KEY_CONSUME_BEER = 2
USER_KEY_CONSUME_SCHORLE = 3
USER_KEY_CONSUME_COLA = 4
USER_KEY_INSERT_COINS = 5
USER_KEY_SHOW_STATS = 6
USER_KEY_ADMINISTRATION = 7
USER_KEY_CHANGE_PASSWORD = 8
USER_KEY_EXIT = 9
USER_KEY_CONSUME_FLORA = 10
USER_KEY_NFC = "N"
USER_KEY_HELP = "?"

user_actions = {
    USER_KEY_CONSUME_MATE: "Consume Club Mate",
    USER_KEY_CONSUME_BEER: "Consume Bier",
    USER_KEY_CONSUME_SCHORLE: "Consume Apfelschorle",
    USER_KEY_CONSUME_COLA: "Consume Mate Cola",
    USER_KEY_INSERT_COINS: "Insert coins",
    USER_KEY_SHOW_STATS: "Show statistics",
    USER_KEY_ADMINISTRATION: "Administration",
    USER_KEY_CHANGE_PASSWORD: "Change password",
    USER_KEY_EXIT: "Exit",
    USER_KEY_CONSUME_FLORA: "[NEU!] Consume Flora Mate",
    USER_KEY_NFC: "Setup NFC Card",
    USER_KEY_HELP: "Help",
}

### Admin Menu Mapping
ADMIN_KEY_LIST_ITEMS = 1
ADMIN_KEY_LIST_USERS = 2
ADMIN_KEY_CREATE_USER = 3
ADMIN_KEY_CREATE_ITEM = 4
ADMIN_KEY_DELETE_ITEM = 5
ADMIN_KEY_RESET_USER_PASSWORD = 6
ADMIN_KEY_SHOW_SERVICE_STATS = 7
ADMIN_KEY_RESET_CREDITS = 8
ADMIN_KEY_EXIT = 9
ADMIN_KEY_DELETE_USER = 10
ADMIN_KEY_MIGRATE_USER = 11
ADMIN_KEY_HELP = "?"

admin_actions = {
    ADMIN_KEY_LIST_ITEMS: "Show drinks",
    ADMIN_KEY_LIST_USERS: "Show users",
    ADMIN_KEY_CREATE_USER: "Create user",
    ADMIN_KEY_CREATE_ITEM: "Create drink",
    ADMIN_KEY_DELETE_ITEM: "Delete drink",
    ADMIN_KEY_RESET_USER_PASSWORD: "Reset password for user",
    ADMIN_KEY_SHOW_SERVICE_STATS: "Show service stats",
    ADMIN_KEY_RESET_CREDITS: "Reset credits from user",
    ADMIN_KEY_EXIT: "Exit",
    ADMIN_KEY_DELETE_USER: "Delete user",
    ADMIN_KEY_MIGRATE_USER: "Migrate user from old Matomat",
    ADMIN_KEY_HELP: "Help",
}

### Functions

def user_menu(auth, auth_client, items_client, users_client, service_client, cfgobj):
    """
    Shows the menu to the user, clears screen, draws the navigation screen
    This is kind of the main loop of heiko. If you need new options, add them here
    otherwise they are not being executed.

    :auth: dict
    :items_client: object
    :users_client: object
    :service_client: object
    :cfgobj: dict

    :returns: is_logged_in, is_exit (both bool)
    """


    optionInput = input(">>> ")
    if len(optionInput) == 0:
        os.system('clear')
        banner(auth)
        option = USER_KEY_HELP
    elif optionInput.isnumeric():
        option = int(optionInput)
    else:
        option = optionInput
    
    
    if option == USER_KEY_CONSUME_MATE:
        consume_item(auth, items_client, 1)
        say(cfgobj, "cheers")

    if option == USER_KEY_CONSUME_BEER:
        consume_item(auth, items_client, 2)
        say(cfgobj, "cheers")

    if option == USER_KEY_CONSUME_SCHORLE:
        consume_item(auth, items_client, 3)
        say(cfgobj, "cheers")

    if option == USER_KEY_CONSUME_COLA:
        consume_item(auth, items_client, 4)
        say(cfgobj, "cheers")

    if option == USER_KEY_INSERT_COINS:
        add_credits(auth, users_client)
        say(cfgobj, "transaction_success")

    if option == USER_KEY_SHOW_STATS:
        show_user_stats(auth, users_client)

    if option == USER_KEY_ADMINISTRATION:
        is_exit = False
        say(cfgobj, "admin")

        draw_help = True
        while is_exit is False:
            is_exit, draw_help = admin_menu(auth, items_client, users_client, service_client, cfgobj, draw_help=draw_help)

        # when exit was executed, draw normal user help again
        os.system('clear')
        banner(auth)
        option = USER_KEY_HELP


    if option == USER_KEY_CHANGE_PASSWORD:
        change_password(auth, users_client)

    if option == USER_KEY_CONSUME_FLORA:
        consume_item(auth, items_client, 7)
        say(cfgobj, "cheers")
        
    if option == USER_KEY_NFC:
        if not cfgobj["nfc"]["enable"]:
            log("NFC is disabled")
            return True, False
        uid = nfc_read()
        if uid is not None:
            ans = input("overwrite card? [yN] ")
            if ans != "y":
                return True, False
            ans = input("token lifetime in days? ")
            if not ans.isnumeric():
                log("invalid lifetime")
                return True, False
            days = int(ans)
            log("re-Login required:")
            password = getpass.getpass('Password: ')
            token = ""
            try:
                auth2 = auth_client.auth_login_post(
                    auth["user"]["username"], password,
                    validityseconds=days*3600*24).to_dict()
                token = auth2["token"]
            except swagger_client.rest.ApiException:
                log("Wrong password!",serv="ERROR")
                return True, False
            except (ConnectionRefusedError, urllib3.exceptions.MaxRetryError):
                log("Connection to backend was refused!",serv="ERROR")
                return True, False
            validstamp = (datetime.now()+timedelta(days=days)).timestamp()
            nfc_write(uid, token)

    if option == USER_KEY_HELP:
        show_help(auth, admin=False)

    if option == USER_KEY_EXIT:
        say(cfgobj, "quit")
        return False, True

    return True, False


def admin_menu(auth, items_client, users_client, service_client, cfgobj, draw_help):
    """
    Shows the menu to the admin, clears screen, draws the navigation screen

    :auth: dict
    :returns: is_logged_in, is_exit (both bool)
    """

    if auth["user"]["admin"] is False:
        say(cfgobj, "error")
        log("Meeeep. Not an administrator, but nice try.", serv="ERROR")
        log("Computer says no.", serv="ERROR")
        return True # is_exit

    try:

        # when logged in the first time, show new menue
        if draw_help is True:
            os.system('clear')
            banner(auth)
            show_help(auth, admin=True)

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

    if option == ADMIN_KEY_SHOW_SERVICE_STATS:
        show_service_stats(auth, service_client)

    if option == ADMIN_KEY_RESET_CREDITS:
        reset_credits(auth, users_client)

    if option == ADMIN_KEY_EXIT:
        say(cfgobj, "quit")
        log("Switching back to normal menu, sir.", serv="SUCCESS")
        return True, False

    if option == ADMIN_KEY_MIGRATE_USER:
        migrate_user(auth, users_client)

    if option == ADMIN_KEY_DELETE_USER:
        delete_user(auth, users_client)
    if option == ADMIN_KEY_HELP:
        show_help(auth, admin=True)

    return False, False

def welcome_banner():
    """
    Prints a big ascii interpretation from the club mate logo

    :returns: bool
    """
    logo_banner = """
                                    =?I777777II?????II777777?=
                               7777?                           I777?
                          I77I     I77               =777777777+     I77=
                      =77I    ?777777=                I7777777777777+   =77+
                   =77=   I7777777777                  77777777777777777+   77?
                 ?77   I7777777777777                  =7777777777777777777   ?77
               77=  I777777777777777?                   7777777777777777777777   77=
             ?7I  ?77777777777777777                     77777777777777777777777   77
           +77  77777777777777777777                     7777777777777777777777777   77
          77   777777777777777777777                      77777777777777777777777777  +7=
         77  77777777777777777777777                      777777777777777777777777777+  77
       I7   777777777777777777777777                          +7777777777777I+= +777777  77
      =7   77777777777777777777?=                   +?77777777777?             ?77777777  77
      7   7777777777=          =7777777777777777777777777=                  7777777777777  7I
     77  77777+                      ==+????++=                         I7777777777777777?  7
    I7  77777777I+                    ?77    ?777?+?7777+       +I777777777777777777777777  77
    7I  77777777777777777777777777    7777   777777777777  = 777777777777777777777777777777  7
    7  77777777777777777777777777+      ?  7 I=777777777 777 =77777777777777777777777777777  77
   77  77777777777777777777777777=777        =+==   I7777 7+ 777777777777777777777777777777  +7
   77  77777777777777777777777777 I? 77         77777=7777777777777777777777777777777777777?  7
   77  77777777777777777777777777777777=   777777777+?77777777777777I7777777777II7777777777I  7
   77  77777777777777777777777777    I       777777 ?777777777777777+7777777777 77777777777+ =7
   ?7  77777777777777777777777?                 77+ 7777777777777777=7777+7777+777777777777  I7
    7  ?777777777777777777I                     +7   =77777777777777+7777 7777 777777777777  7?
    77  777777777777777                                 77777777777+77777 77 I=77777777777+  7
     7  +777777777777                                     777777777 777=77+77I777777777777  7I
     77  I777777777                                        +7777=77=777?=777 777777777777  I7
      77  7777777                                            7 777=?777777? I77777777777=  7
       77  I777                                              77777777777    77777777777   7
        77  ?                                              ?777777777777I  77777777777   7
         ?7                                               777777777777777I77777777777  77
           77                                             777777777777I==I777777777=  7I
            +7+                                           77777      ?77777777777+  77
              +7+                                         777         ?77777777   77
                77=                                       77           +77777   77=
                   77                                                    7   I7?
                     77I                                                   77
                        +77?                                           77I
                            +77I                                  =777=
                                  7777I+                   ?7777+
                                          ++?IIII7III??+=

                    When your login does not work - you need to be migrated :)
                     github.com/k4cg/heiko / github.com/k4cg/matomat-service
"""
    log(logo_banner)
    return True

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


def login(auth_client, cfgobj):
    """
    Shows banner, asks user to authenticate via username/password
    and creates auth token that we reuse after auth was successful once.

    :returns: tuple
    """
    is_logged_in = False
    auth = None

    os.system('clear')
    welcome_banner()
    log("Please authenticate yourself!")

    try:
        user = input('User: ')
        password = getpass.getpass('Password: ')
    except EOFError:
        say(cfgobj, "error")
        return is_logged_in, auth

    try:
        auth = auth_client.auth_login_post(user, password).to_dict()
        is_logged_in = True
        greet_user(cfgobj, auth["user"]["username"])
    except swagger_client.rest.ApiException:
        say(cfgobj, "error")
        log("Wrong username and/or password!",serv="ERROR")
        time.sleep(1)
    except (ConnectionRefusedError, urllib3.exceptions.MaxRetryError):
        say(cfgobj, "error")
        log("Connection to backend was refused!",serv="ERROR")
        time.sleep(5)


    return is_logged_in, auth

