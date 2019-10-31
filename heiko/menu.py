import time
import getpass
import os
import urllib3
import select
import sys
import base64
import json
import binascii
import signal
import pkg_resources

import swagger_client
from heiko.items import list_items_stats, consume_item, create_item, delete_item, update_item
from heiko.users import add_credits, add_credits_admin, list_users, create_user, create_user_nfc, reset_user_password, reset_user_nfc, delete_user, reset_credits, change_password, show_user_stats, transfer_coins
from heiko.service import show_service_stats
from heiko.utils import log
from heiko.voice import say, greet_user
from heiko.migrate import migrate_user
from heiko.nfc import nfc_detect, nfc_read, nfc_format_card

# User Menu Mapping
USER_KEY_INSERT_COINS = "i"
USER_KEY_TRANSFER_COINS = "t"
USER_KEY_SHOW_STATS = "s"
USER_KEY_ADMINISTRATION = "a"
USER_KEY_CHANGE_PASSWORD = "p"
USER_KEY_EXIT = "x"
USER_KEY_NFC = "n"
USER_KEY_HELP = "?"

user_actions = {
    USER_KEY_INSERT_COINS: "Insert coins",
    USER_KEY_TRANSFER_COINS: "Transfer coins",
    USER_KEY_SHOW_STATS: "Show statistics",
    USER_KEY_ADMINISTRATION: "Administration",
    USER_KEY_CHANGE_PASSWORD: "Change password",
    USER_KEY_EXIT: "Exit",
    USER_KEY_NFC: "Setup NFC Card",
    USER_KEY_HELP: "Help",
}

consumables = {}

# Seconds to automatic logout:
AUTOLOGOUT_TIME_SECONDS = 120

# Admin Menu Mapping
ADMIN_KEY_LIST_ITEMS_STATS = "l"
ADMIN_KEY_LIST_USERS = "u"
ADMIN_KEY_CREATE_USER = "cu"
ADMIN_KEY_CREATE_USER_NFC = "cun"
ADMIN_KEY_CREATE_ITEM = "ci"
ADMIN_KEY_DELETE_ITEM = "di"
ADMIN_KEY_UPDATE_ITEM = "ui"
ADMIN_KEY_RESET_USER_PASSWORD = "ru"
ADMIN_KEY_RESET_USER_NFC = "run"
ADMIN_KEY_SHOW_SERVICE_STATS = "ss"
ADMIN_KEY_RESET_CREDITS = "r"
ADMIN_KEY_ADD_CREDITS = "a"
ADMIN_KEY_EXIT = "x"
ADMIN_KEY_DELETE_USER = "du"
ADMIN_KEY_MIGRATE_USER = "m"
ADMIN_KEY_HELP = "?"

admin_actions = {
    ADMIN_KEY_LIST_ITEMS_STATS: "Show drinks stats",
    ADMIN_KEY_LIST_USERS: "Show users",
    ADMIN_KEY_CREATE_USER: "Create user",
    ADMIN_KEY_CREATE_USER_NFC: "Create user with NFC card and dummy random password",
    ADMIN_KEY_CREATE_ITEM: "Create drink",
    ADMIN_KEY_DELETE_ITEM: "Delete drink",
    ADMIN_KEY_UPDATE_ITEM: "Update drink",
    ADMIN_KEY_RESET_USER_PASSWORD: "Reset password for user",
    ADMIN_KEY_RESET_USER_NFC: "Reset password + setup NFC card for user",
    ADMIN_KEY_SHOW_SERVICE_STATS: "Show service stats",
    ADMIN_KEY_RESET_CREDITS: "Reset credits from user",
    ADMIN_KEY_ADD_CREDITS: "Add credits for user",
    ADMIN_KEY_EXIT: "Exit",
    ADMIN_KEY_DELETE_USER: "Delete user",
    ADMIN_KEY_MIGRATE_USER: "Migrate user from old Matomat",
    ADMIN_KEY_HELP: "Help",
}

# Functions


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
    signal.alarm(AUTOLOGOUT_TIME_SECONDS)

    try:
        optionInput = input(">>> ")
        if optionInput not in user_actions.keys() and optionInput not in consumables.keys():
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

    if option == USER_KEY_TRANSFER_COINS:
        transfer_coins(auth, users_client)

    if option == USER_KEY_ADMINISTRATION:
        is_exit = False
        say(cfgobj, "admin")

        draw_help = True
        while is_exit is False:
            is_exit, draw_help = admin_menu(auth, auth_client, items_client, users_client, service_client, cfgobj, draw_help=draw_help)

        # when exit was executed, draw normal user help again
        option = USER_KEY_HELP

    if option == USER_KEY_CHANGE_PASSWORD:
        change_password(auth, users_client)

    if option == USER_KEY_NFC:
        username = auth["user"]["username"]
        log("Put your card on the reader now.")
        log("Relogin required:")
        password = getpass.getpass('Password: ')
        nfc_format_card(auth_client, username, password)

    if option == USER_KEY_HELP:
        banner(auth)
        show_help(items_client, admin=False, cfgobj=cfgobj)

    if option == USER_KEY_EXIT:
        return user_exit(cfgobj)

    return True, False


def user_exit(cfgobj):
    say(cfgobj, "quit")
    return False, True


def admin_menu(auth, auth_client, items_client, users_client, service_client, cfgobj, draw_help):
    """
    Shows the menu to the admin, clears screen, draws the navigation screen

    :auth: dict
    :returns: is_logged_in, is_exit (both bool)
    """

    signal.alarm(AUTOLOGOUT_TIME_SECONDS)

    if auth["user"]["admin"] is False:
        say(cfgobj, "error")
        log("Meeeep. Not an administrator, but nice try.", serv="ERROR")
        log("Computer says no.", serv="ERROR")
        time.sleep(5)
        return True, True

    try:
        # when logged in the first time, show new menue
        if draw_help is True:
            banner(auth)
            show_help(items_client, admin=True, cfgobj=cfgobj)

        optionInput = input(">>> ")
        if optionInput not in admin_actions.keys():
            option = ADMIN_KEY_HELP
        else:
            option = optionInput
    except EOFError:
        return admin_exit(cfgobj)

    if option == ADMIN_KEY_LIST_ITEMS_STATS:
        list_items_stats(auth, items_client)

    if option == ADMIN_KEY_LIST_USERS:
        list_users(auth, users_client)

    if option == ADMIN_KEY_CREATE_USER:
        create_user(auth, users_client)

    if option == ADMIN_KEY_CREATE_USER_NFC:
        create_user_nfc(auth_client, users_client)

    if option == ADMIN_KEY_CREATE_ITEM:
        create_item(auth, items_client)

    if option == ADMIN_KEY_DELETE_ITEM:
        delete_item(auth, items_client)

    if option == ADMIN_KEY_UPDATE_ITEM:
        update_item(auth, items_client)

    if option == ADMIN_KEY_RESET_USER_PASSWORD:
        reset_user_password(auth, users_client)

    if option == ADMIN_KEY_RESET_USER_NFC:
        reset_user_nfc(auth, auth_client, users_client)

    if option == ADMIN_KEY_SHOW_SERVICE_STATS:
        show_service_stats(auth, service_client)

    if option == ADMIN_KEY_RESET_CREDITS:
        reset_credits(auth, users_client)

    if option == ADMIN_KEY_ADD_CREDITS:
        add_credits_admin(auth, users_client)

    if option == ADMIN_KEY_EXIT:
        return admin_exit(cfgobj)

    if option == ADMIN_KEY_MIGRATE_USER:
        migrate_user(auth, users_client, cfgobj)

    if option == ADMIN_KEY_DELETE_USER:
        delete_user(auth, users_client)

    if option == ADMIN_KEY_HELP:
        banner(auth)
        show_help(items_client, admin=True, cfgobj=cfgobj)

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

                     github.com/k4cg/heiko (v{}) / github.com/k4cg/matomat-service
""".format(pkg_resources.require("heiko")[0].version)
    os.system('clear')
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
    os.system('clear')
    log(mate_banner)
    if auth is not None:
        if auth["user"]["admin"] is True:
            log("Hi %s, current credits: %.2f Euro. You are admin!\n" % (auth["user"]["username"], auth["user"]["credits"] / 100))
        else:
            log("Hi %s, current credits: %.2f Euro.\n" % (auth["user"]["username"], auth["user"]["credits"] / 100))

    return True


def show_help(items_client, admin=False, cfgobj=None):
    """
    Shows the basic navigation to the user.

    :items_client: object
    :admin: bool
    :returns: bool
    """

    if admin is True:
        actions = admin_actions.copy()
    else:
        actions = user_actions.copy()

        try:
            if cfgobj["accounting"]["user_can_add_credits"] is False:
                del actions[USER_KEY_INSERT_COINS]
        except KeyError:
            pass

        # Reset consumables, to avoid stale entries:
        consumables.clear()

        try:
            for item in items_client.items_get():
                item_dict = item.to_dict()
                action_key = str(item_dict["id"])
                consumables.update({action_key: item_dict})
                actions.update({action_key: "Consume {} ({:.2f})".format(item_dict['name'], item_dict['cost'] / 100)})
        except swagger_client.rest.ApiException:
            log("Could not get items from the database.", serv="ERROR")

    log("Available actions:")
    for key in sorted(actions.keys()):
        log("[%s] %s" % (key, actions[key]))

    return True


def login(maas_builder, auth_client, cfgobj):
    """
    Shows banner, asks user to authenticate via username/password
    and creates auth token that we reuse after auth was successful once.

    :returns: tuple
    """
    is_logged_in = False
    auth = None

    welcome_banner()
    log("Please authenticate yourself!")

    token = ""
    user = ""
    password = ""
    try:
        print("User: ", end="", flush=True)
        uid = ""
        if cfgobj['nfc']['enable']:
            while sys.stdin not in select.select([sys.stdin], [], [], 0)[0]:
                uid, header = nfc_detect()
                if uid:
                    break
                time.sleep(0.2)
        if uid:
            token = nfc_read(uid)
        else:
            user = sys.stdin.readline().strip()
            password = getpass.getpass('Password: ')
    except EOFError:
        say(cfgobj, "error")
        return is_logged_in, auth

    if token:
        t = token.split(".")[1]
        try:
            userdict = json.loads(base64.b64decode(t + "=" * (4 - len(t) % 4)).decode())
        except json.JSONDecodeError:
            say(cfgobj, "error")
            log("Token json error!", serv="ERROR")
            time.sleep(1)
        except binascii.Error:
            say(cfgobj, "error")
            log("Token base64 error!", serv="ERROR")
            time.sleep(1)

        auth = {"token": token, "user": userdict}

        try:
            users_client = maas_builder.build_users_client(auth["token"])
            tmp = users_client.users_user_id_get(userdict["id"]).to_dict()
            for key in tmp:
                auth["user"][key] = tmp[key]
            is_logged_in = True
            greet_user(cfgobj, auth["user"]["username"])
        except swagger_client.rest.ApiException:
            say(cfgobj, "error")
            log("Invalid token!", serv="ERROR")
            time.sleep(1)
        except (ConnectionRefusedError, urllib3.exceptions.MaxRetryError):
            say(cfgobj, "error")
            log("Connection to backend was refused!", serv="ERROR")
            time.sleep(5)
    else:
        try:
            auth = auth_client.auth_login_post(user, password).to_dict()
            is_logged_in = True
            greet_user(cfgobj, auth["user"]["username"])
        except swagger_client.rest.ApiException:
            say(cfgobj, "error")
            log("Wrong username and/or password!", serv="ERROR")
            time.sleep(1)
        except (ConnectionRefusedError, urllib3.exceptions.MaxRetryError):
            say(cfgobj, "error")
            log("Connection to backend was refused!", serv="ERROR")
            time.sleep(5)

    return is_logged_in, auth
