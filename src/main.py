import logging

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from src.config_provider import FileConfigProvider
from src.password_breaker import PasswordBreaker
from src.report_generator import ReportGenerator


def main():
    logging.basicConfig(level=logging.DEBUG)
    logging.debug("Initializing")
    config_provider = FileConfigProvider()
    password_breaker = PasswordBreaker()
    report_generator = ReportGenerator()

    logging.debug("Getting config")
    website_config = config_provider.provide("test_config.json")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(website_config.url)

    logging.debug("Brutforce breaking start")
    correct_password, breaking_duration = password_breaker.find_correct_password(driver=driver,
                                                                                 website_config=website_config)
    logging.debug("Brutforce breaking end")
    driver.close()

    logging.debug("Saving report to file")
    report_generator.generate_report(correct_password, website_config, breaking_duration)


if __name__ == "__main__":
    main()
