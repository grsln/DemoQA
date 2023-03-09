from allure import step
from selenium.webdriver.common.by import By

from browser import browser
from pages.base_page import BasePage


class LeftMenu(BasePage):
    @staticmethod
    def group(group_name):
        return browser.driver.find_element(
            By.XPATH,
            f"//div[text()='{group_name}']/ancestor::div[@class='element-group']",
        )

    @step('Открытие пункта "{item_name}" левого меню')
    def click_item(self, item_name):
        return self.click(By.XPATH, f"//li/span[text()='{item_name}']")

    @step('Проверка раскрытия группы "{group_name}" пунктов меню')
    def is_expanded_group(self, group_name):
        return self.group(group_name).find_elements(By.CSS_SELECTOR, ".show")


left_menu = LeftMenu()
