from allure import step

from pages.base_page import BasePage
from pages.components.checkbox_tree import checkbox_tree
from pages.components.left_menu import left_menu


class CheckBoxPage(BasePage):
    def __init__(self):
        self.left_menu = left_menu
        self.checkbox_tree = checkbox_tree

    @step("Проверка выбора чекбокса Word File.doc")
    def assert_word_file_selected(self):
        assert checkbox_page.checkbox_tree.is_selected_checkbox_word_file()

    @step('Проверка вывода сообщения "You have selected : wordFile"')
    def assert_show_message(self):
        assert (
            checkbox_page.checkbox_tree.get_message() == "You have selected :\nwordFile"
        )


checkbox_page = CheckBoxPage()
