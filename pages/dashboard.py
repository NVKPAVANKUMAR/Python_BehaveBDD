from selenium.common.exceptions import NoSuchElementException

from locators.weblocators import WebLocators as Loc


class DashboardPage:

    def __init__(self, context):
        self.driver = context

    def assert_title_text(self, expected):
        assert self.driver.find_by_xpath(Loc.dashboard_title_text).text.strip() == expected
