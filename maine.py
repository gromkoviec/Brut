from Cracker import Cracker

if __name__ == "__main__":
    password_path = "./passw"
    user_login = "test"
    url = "http://testphp.vulnweb.com/login.php"
    cracker = Cracker(password_path, user_login, url)

    user_space = "uname"
    password_space = "pass"
    cssclick = "#content > div:nth-child(1) > form > table > tbody > tr:nth-child(3) > td > input[type=submit]"
    cracker.login(user_space, password_space, cssclick)
