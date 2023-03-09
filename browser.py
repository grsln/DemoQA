from typing import Union

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver as WebDriverChrome
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.webdriver import WebDriver as WebDriverFirefox
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

TypeDriver = Union[WebDriverChrome, WebDriverFirefox, None]


class Browser:
    def __init__(self):
        self.driver: TypeDriver = None

    def set_driver(self, browser_name):
        if browser_name == "chrome":
            self.driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install())
            )
        if browser_name == "firefox":
            self.driver = webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install())
            )

        if not self.driver:
            raise Exception("Не установлен драйвер браузера")


browser = Browser()
