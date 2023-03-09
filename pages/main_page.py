from allure import step
from selenium.webdriver.common.by import By

from browser import browser
from common.constants import BASE_URL
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self):
        self.url = BASE_URL

    @step("Нажатие кнопки {name}")
    def click_card(self, name):
        self.click(
            By.XPATH,
            f"//h5[text()='{name}']/ancestor::div[contains(@class,'top-card')]",
        )

    @step("Открытие главной страницы")
    def open(self):
        browser.driver.get(self.url)


main_page = MainPage()
