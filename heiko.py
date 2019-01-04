#!/usr/bin/env python3

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

banner = """
 __  __    _  _____ ___  __  __    _  _____
|  \/  |  / \|_   _/ _ \|  \/  |  / \|_   _|
| |\/| | / _ \ | || | | | |\/| | / _ \ | |
| |  | |/ ___ \| || |_| | |  | |/ ___ \| |
|_|  |_/_/   \_\_| \___/|_|  |_/_/   \_\_|

"""

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

    log(banner)

    print("Available actions:")
    for key in actions.keys():
        print("[%s] %s" % (key, actions[key]))



def login():
    """
    Clear screen and show prompt
    :returns: tupel
    """
    auth_client = maas_builder.build_auth_api_client()

    print(chr(27) + "[2J")

    log(banner)
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

def prompt(auth):

    print(chr(27) + "[2J")
    log(banner)
    token = auth["token"]

    return True

if __name__ == '__main__':
    maas_cfg = MaaSConfig("https://localhost:8443/v0", False)
    maas_builder = MaaSApiClientBuilder(maas_cfg)

    # This is the login loop.

    is_logged_in = False
    while is_logged_in is False:
        is_logged_in, auth = login()

    prompt(auth)

    items_client = maas_builder.build_items_client(token)
    # response = items_client.items_post("mate", 100)
    # print(response)

    response = items_client.items_get()
    print(swagger_client.Item(response))


