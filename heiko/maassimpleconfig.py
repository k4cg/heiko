import yaml


class MaasSimpleConfig:

    def __init__(self):
        self.__config = []

    def load(self, file_path):
        self.__config = []
        with open(file_path, 'r') as stream:
            try:
                self.__config = yaml.load(stream)
            except yaml.YAMLError as exc:
                print(exc)
        return self

    def get_maas_host(self) -> str:
        return self.__config['maas']['host']

    def get_maas_server_port(self) -> int:
        return self.__config['maas']['port']

    def get_maas_api_url_base_path(self) -> str:
        return self.__config['maas']['api_url_base_path']

    def get_maas_verify_ssl_certificates(self) -> bool:
        return self.__config['maas']['verify_ssl_certificates']

    def get_all(self) -> dict:
        return self.__config
