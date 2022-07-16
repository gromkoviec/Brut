import json
from os.path import exists, join

from src.dir_constans import CONFIG_DIR
from src.website_config import WebsiteConfig


class ConfigProvider:
    def provide(self, path):
        raise Exception("Use class that inherit from this one")

    def validate(self, dom):
        raise Exception("Use class that inherit from this one")
        # TODO implement selector validation
        pass


class FileConfigProvider(ConfigProvider):
    def provide(self, path):
        file_path = path
        config_dir = CONFIG_DIR
        if not exists(path):
            if exists(join(config_dir, path)):
                file_path = join(config_dir, path)
            else:
                raise Exception(f'Config not found for path {path}')

        with open(file_path, "r") as fp:
            return json.load(fp, object_hook=lambda d: WebsiteConfig(**d))

    def validate(self, dom):
        # TODO implement selector validation
        pass


class TerminalConfigProvider(ConfigProvider):
    def provide(self, path) -> WebsiteConfig:
        url = self.get_url()
        login_username = self.get_username()
        passwords_file_path = self.get_password_file_name()
        username_selector = self.get_username_selector()
        password_selector = self.get_password_selector()
        submit_button_selector = self.get_submit_button_selector()
        return WebsiteConfig(url=url,
                             login_username=login_username,
                             passwords_file_name=passwords_file_path,
                             username_selector=username_selector,
                             password_selector=password_selector,
                             submit_button_selector=submit_button_selector)

    def get_url(self) -> str:
        site = input("Podaj adres strony:")
        if site == "test":
            site = "http://testphp.vulnweb.com/login.php"
        else:
            site = site
        return site

    def get_username(self) -> str:
        username = input("Podaj nazwę użytkownika:")
        if username != "":
            pass
        else:
            print("Nazwa użytkownika nie może być pusta:")
        return username

    def get_password_file_name(self) -> str:
        passfile = input("Podaj nazwę pliku haseł :")
        if passfile == "":
            passfile = "pass_list"
        else:
            passfile = passfile
        return passfile

    def get_submit_button_selector(self) -> str:
        return "#content > div:nth-child(1) > form > table > tbody > tr:nth-child(3) > td > input[type=submit]"

    def get_username_selector(self):
        username_driver = input("Podaj nazwę elmentu z nazwą użytkownika: ")
        if username_driver == "":
            username_driver = "uname"
        else:
            username_driver = username_driver
        return username_driver

    def get_password_selector(self):
        password_driver = input("Podaj nazwę elmentu z hasłem: ")
        if password_driver == "":
            password_driver = "pass"
        else:
            password_driver = password_driver
        return password_driver
