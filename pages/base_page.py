from browser import browser


class BasePage:
    @staticmethod
    def click(by, value):
        browser.driver.find_element(by, value).click()

    @staticmethod
    def get_text(by, value):
        return browser.driver.find_element(by, value).text

    @staticmethod
    def is_selected(by, value):
        return browser.driver.find_element(by, value).is_selected()
