#!/usr/bin/env python3

import os
import json
import time
import getpass
import swagger_client

# temp for annoying error msg
import urllib3
urllib3.disable_warnings()


# Menu Mapping
KEY_LIST_ITEMS = 1
KEY_CONSUME_MATE = 2
KEY_CONSUME_BEER = 3
KEY_LIST_USERS = 4
KEY_INSERT_COINS = 5
KEY_HELP = 8
KEY_EXIT = 9

actions = {
    KEY_LIST_ITEMS: "Show drinks",
    KEY_CONSUME_MATE: "Consume Mate",
    KEY_CONSUME_BEER: "Consume Beer",
    KEY_LIST_USERS: "Show users",
    KEY_INSERT_COINS: "Insert coins",
    KEY_HELP: "Help",
    KEY_EXIT: "Exit",
}

class MaaSConfig:
    def __init__(self, host, verify_ssl):
        self.host = host
        self.verify_ssl = verify_ssl

class MaaSApiClientBuilder:
    def __init__(self, config: MaaSConfig):
        super().__init__()
        self._maas_config = config

    def build_auth_api_client(self):
        # create an instance of the API class
        return swagger_client.AuthApi(swagger_client.ApiClient(self.build_config()))

    def build_items_client(self, token):
        return swagger_client.ItemsApi(swagger_client.ApiClient(self.build_config_with_token(token)))

    def build_users_client(self, token):
        return swagger_client.UsersApi(swagger_client.ApiClient(self.build_config_with_token(token)))

    def build_config(self):
        # create an configuration for the general API client
        api_client_config = swagger_client.Configuration()
        api_client_config.host = self._maas_config.host
        api_client_config.verify_ssl = self._maas_config.verify_ssl

        return api_client_config

    def build_config_with_token(self, token):
        api_client_config = swagger_client.Configuration()
        api_client_config.host = self._maas_config.host
        api_client_config.verify_ssl = self._maas_config.verify_ssl
        api_client_config.api_key = {
            'Authorization': token
        }
        api_client_config.api_key_prefix = {
            'Authorization': 'Bearer'
        }

        return api_client_config

def log(msg, serv="INFO"):
    print(msg)

def help():

    log("Available actions:")
    for key in actions.keys():
        log("[%s] %s" % (key, actions[key]))


def login():
    """
    Clear screen and show prompt
    :returns: tupel
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


def list_items(auth):
    items_client = maas_builder.build_items_client(auth["token"])
    log(items_client.items_get())

def list_users(auth):
    users_client = maas_builder.build_users_client(auth["token"])
    users = users_client.users_get()

    log("List of current users in the database:\n")
    log("ID\tCredits\tUsername")
    for user in users:
        user = user.to_dict()
        log("%s\t%s\t%s" % (user["id"], user["credits"], user["username"]))

def insert_coins(auth, credits):

    cents = int(credits) * 100
    users_client = maas_builder.build_users_client(auth["token"])
    users_client.users_user_id_credits_add_patch(auth["user"]["id"], cents)

    log("Your credit is now %.2f" % (r["credits"]/100))
        # print("EUR input can range from 1 to 100")


def show_coins(auth):

    users_client = maas_builder.build_users_client(auth["token"])
    users_client
    return

def banner(auth=None):

    mate_banner = """
 __  __    _  _____ ___  __  __    _  _____
|  \/  |  / \|_   _/ _ \|  \/  |  / \|_   _|
| |\/| | / _ \ | || | | | |\/| | / _ \ | |
| |  | |/ ___ \| || |_| | |  | |/ ___ \| |
|_|  |_/_/   \_\_| \___/|_|  |_/_/   \_\_|
"""
    log(mate_banner)
    if auth is not None:
        log("Hi %s, current credits: %s\n" % (auth["user"]["username"], auth["user"]["credits"]))

def menu(auth):

    try:
        option = int(input(">>> "))
    except ValueError:
        os.system('clear')
        banner(auth)
        option = KEY_HELP

    # Normal users menu
    if option == KEY_LIST_ITEMS:
        list_items(auth)
    if option == KEY_CONSUME_MATE:
        consume(auth['token'], 1)
    if option == KEY_CONSUME_BEER:
        consume(auth['token'], 2)
    if option == KEY_INSERT_COINS:
        coins = input("EUR: ")
        insert_coins(auth, coins)
    if option == KEY_HELP:
        help()

    # Admin options
    if auth["user"]["admin"] is True:
        if option == KEY_LIST_USERS:
            list_users(auth)

    if option == KEY_EXIT:
        return False, True

    return True, False

if __name__ == '__main__':

    maas_cfg = MaaSConfig("https://localhost:8443/v0", False)
    maas_builder = MaaSApiClientBuilder(maas_cfg)

    # This is the login loop.
    is_logged_in = False
    while is_logged_in is False:
        is_logged_in, auth = login()
        os.system('clear')
        banner(auth)
        help()

        # When autenticated go to menu
        is_exit = False
        while is_exit is False:
            is_logged_in, is_exit = menu(auth)

