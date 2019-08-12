import time
import getpass
import os
import urllib3
import pprint

import swagger_client
from heiko.items import list_items_stats, consume_item, create_item, delete_item
from heiko.users import add_credits, list_users, create_user, reset_user_password, delete_user, reset_credits, change_password, show_user_stats
from heiko.service import show_service_stats
from heiko.utils import log
from heiko.voice import say, greet_user
from heiko.migrate import migrate_user
from heiko.nfc import nfc_read, nfc_write

from datetime import datetime, timedelta

### User Menu Mapping
USER_KEY_INSERT_COINS = "i"
USER_KEY_SHOW_STATS = "s"
USER_KEY_ADMINISTRATION = "a"
USER_KEY_CHANGE_PASSWORD = "p"
USER_KEY_EXIT = "x"
USER_KEY_NFC = "n"
USER_KEY_HELP = "?"

user_actions = {
    USER_KEY_INSERT_COINS: "Insert coins",
    USER_KEY_SHOW_STATS: "Show statistics",
    USER_KEY_ADMINISTRATION: "Administration",
    USER_KEY_CHANGE_PASSWORD: "Change password",
    USER_KEY_EXIT: "Exit",
    USER_KEY_NFC: "Setup NFC Card",
    USER_KEY_HELP: "Help",
}

consumables = {}

### Admin Menu Mapping
ADMIN_KEY_LIST_ITEMS_STATS = "l"
ADMIN_KEY_LIST_USERS = "u"
ADMIN_KEY_CREATE_USER = "cu"
ADMIN_KEY_CREATE_ITEM = "ci"
ADMIN_KEY_DELETE_ITEM = "di"
ADMIN_KEY_RESET_USER_PASSWORD = "ru"
ADMIN_KEY_SHOW_SERVICE_STATS = "ss"
ADMIN_KEY_RESET_CREDITS = "r"
ADMIN_KEY_EXIT = "x"
ADMIN_KEY_DELETE_USER = "du"
ADMIN_KEY_MIGRATE_USER = "m"
ADMIN_KEY_HELP = "?"

admin_actions = {
    ADMIN_KEY_LIST_ITEMS_STATS: "Show drinks stats",
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

    try:
        optionInput = input(">>> ")
        if len(optionInput) == 0:
            os.system('clear')
            banner(auth)
            option = USER_KEY_HELP
        elif not optionInput in user_actions.keys() and not optionInput in consumables.keys():
            os.system('clear')
            banner(auth)
            option = USER_KEY_HELP
        else:
            option = optionInput
    except EOFError:
        return user_exit(cfgobj)

    if option in consumables.keys():
        consume_item(auth, items_client, consumables[option]['id'])
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
        show_help(items_client, admin=False)

    if option == USER_KEY_EXIT:
        return user_exit(cfgobj)

    return True, False


def user_exit(cfgobj):
    say(cfgobj, "quit")
    return False, True


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
        time.sleep(5)
        return True, True

    try:

        # when logged in the first time, show new menue
        if draw_help is True:
            os.system('clear')
            banner(auth)
            show_help(items_client, admin=True)

        option = input(">>> ")
    except ValueError:
        os.system('clear')
        banner(auth)
        option = ADMIN_KEY_HELP
    except EOFError:
        return admin_exit(cfgobj)

    if option == ADMIN_KEY_LIST_ITEMS_STATS:
        list_items_stats(auth, items_client)

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
        return admin_exit(cfgobj)

    if option == ADMIN_KEY_MIGRATE_USER:
        migrate_user(auth, users_client)

    if option == ADMIN_KEY_DELETE_USER:
        delete_user(auth, users_client)
    if option == ADMIN_KEY_HELP:
        show_help(items_client, admin=True)

    return False, False


def admin_exit(cfgobj):
    say(cfgobj, "quit")
    log("Switching back to normal menu, sir.", serv="SUCCESS")
    return True, False


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


def show_help(items_client, admin=False):
    """
    Shows the basic navigation to the user.

    :items_client: object
    :admin: bool
    :returns: bool
    """

    if admin is True:
        actions = admin_actions
    else:
        actions = user_actions.copy()

        # Reset consumables, to avoid stale entries:
        consumables.clear()

        try:
            for item in items_client.items_get():
                item_dict = item.to_dict()
                action_key = str(item_dict["id"])
                consumables.update({action_key: item_dict})
                actions.update({action_key: "Consume " + item_dict['name']})
        except swagger_client.rest.ApiException:
            log("Could not get items from the database.",serv="ERROR")

    log("Available actions:")
    for key in sorted(actions.keys()):
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
        # FIXME This does not work
        auth = auth_client.auth_login_post(user, password, validityseconds=42)
        pprint.pprint(auth)
        exit(1)
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

