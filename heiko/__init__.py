import argparse
import swagger_client
import sys
import os
import signal
import urllib3
from heiko.menu import user_menu, banner, login, show_help
from heiko.maassimpleconfig import MaasSimpleConfig
from heiko.nfc import nfc_init
from heiko.utils import log


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

    def build_service_client(self, token):
        return swagger_client.ServiceApi(swagger_client.ApiClient(self.build_config_with_token(token)))

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


def sigint_handler(signal, frame):
    print("\n")
    sys.exit(0)


def sigalrm_handler(signal, frame):
    log("\nAuto-logout timer triggered!")
    sys.exit(1)


signal.signal(signal.SIGINT, sigint_handler)
signal.signal(signal.SIGALRM, sigalrm_handler)


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--nfctty', type=str, default="any")
    args = parser.parse_args()

    urllib3.disable_warnings()
    cfg = MaasSimpleConfig().load('config.yml')
    conn_str = 'https://' + cfg.get_maas_host() + ':' + str(cfg.get_maas_server_port()) + cfg.get_maas_api_url_base_path()
    maas_cfg = MaaSConfig(conn_str, cfg.get_maas_verify_ssl_certificates())
    maas_builder = MaaSApiClientBuilder(maas_cfg)

    cfgobj = cfg.get_all()

    if cfgobj["nfc"]["enable"]:
        # Only enable NFC on the real matomat TTY, to avoid locking conflicts
        if args.nfctty == "any" or os.ttyname(sys.stdout.fileno()) == args.nfctty:
            nfc_init()
        else:
            cfgobj["nfc"]["enable"] = False

    # This is the login loop.
    is_logged_in = False
    while is_logged_in is False:

        auth_client = maas_builder.build_auth_api_client()
        is_logged_in, auth = login(maas_builder, auth_client, cfgobj)

        if is_logged_in is False:
            continue

        if auth is not None:
            items_client = maas_builder.build_items_client(auth["token"])
            users_client = maas_builder.build_users_client(auth["token"])
            service_client = maas_builder.build_service_client(auth["token"])

        banner(auth)
        show_help(items_client, False, cfgobj)

        # When autenticated go to menu
        is_exit = False
        while is_exit is False:
            is_logged_in, is_exit = user_menu(auth, auth_client, items_client, users_client, service_client, cfgobj)
            # Cancel autologout timer:
            signal.alarm(0)


if __name__ == '__main__':
    main()
