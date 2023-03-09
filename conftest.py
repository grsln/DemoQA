import logging

import allure
import pytest

from browser import browser

BROWSERS_LIST = ["chrome", "firefox"]

logger = logging.getLogger("demoqa")


@pytest.fixture(params=BROWSERS_LIST, autouse=True)
def driver(request):
    browser.set_driver(request.param)
    browser.driver.maximize_window()
    browser.driver.implicitly_wait(3)
    yield browser
    browser.driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.failed:
        try:
            allure.attach(
                browser.driver.get_screenshot_as_png(),
                name="Screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
            allure.attach(
                browser.driver.page_source,
                name="Page source",
                attachment_type=allure.attachment_type.TEXT,
            )
        except Exception as e:
            logger.error("Fail to take screen-shot and save page source: {}".format(e))
