from allure import step
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckBoxTree(BasePage):
    def __init__(self):
        self.home_toggle = (
            By.XPATH,
            "//*[@id='tree-node-home']/parent::*/preceding-sibling::button",
        )
        self.downloads_toggle = (
            By.XPATH,
            "//*[@id='tree-node-downloads']/parent::*/preceding-sibling::button",
        )
        self.word_file_toggle = (
            By.XPATH,
            "//*[@id='tree-node-wordFile']/parent::*/preceding-sibling::button",
        )
        self.word_file_label = (By.XPATH, "//*[@id='tree-node-wordFile']/parent::label")
        self.word_file_checkbox = (By.CSS_SELECTOR, "#tree-node-wordFile")
        self.result_message = (By.ID, "result")

    @step("Выделение чекбокса Word File.doc")
    def select_word_file(self):
        self.click(*self.home_toggle)
        self.click(*self.downloads_toggle)
        self.click(*self.word_file_label)

    def get_message(self):
        return self.get_text(*self.result_message)

    def is_selected_checkbox_word_file(self):
        return self.is_selected(*self.word_file_checkbox)


checkbox_tree = CheckBoxTree()
