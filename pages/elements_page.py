from pages.base_page import BasePage
from pages.components.left_menu import left_menu


class ElementsPage(BasePage):
    def __init__(self):
        self.left_menu = left_menu


elements_page = ElementsPage()
