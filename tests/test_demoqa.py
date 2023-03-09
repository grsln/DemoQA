import allure
import pytest
from allure_commons.types import Severity

from pages.checkbox_page import checkbox_page
from pages.elements_page import elements_page
from pages.main_page import main_page


@allure.severity(Severity.NORMAL)
@pytest.mark.smoke
def test_select_checkbox():
    main_page.open()
    main_page.click_card("Elements")
    elements_page.left_menu.click_item("Check Box")
    checkbox_page.checkbox_tree.select_word_file()
    checkbox_page.assert_word_file_selected()
    checkbox_page.assert_show_message()
