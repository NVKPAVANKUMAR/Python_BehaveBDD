from behave import given, when, then
import configparser
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from pages.login import LoginPage
from pages.dashboard import DashboardPage
import unittest


def parse_config(header, parameter):
    config = configparser.ConfigParser()
    config.read('configuration/config.ini')
    return config.get(header, parameter)


@given('user is on DemoLoginpage')
def navigate_login_page(context):
    context.browser.visit(parse_config('Credentials', 'url'))


@when('user enters valid {username} and {password}')
def step_impl(context, username, password):
    login_page = LoginPage(context.browser)
    login_page.enter_username(username)
    login_page.enter_password(password)


@when('clicks on signin button')
def step_impl(context):
    login_page = LoginPage(context.browser)
    login_page.click_signin()


@then('user navigates to Demodashboardpage')
def step_impl(context):
    try:
        dashboard_page = DashboardPage(context.browser)
        dashboard_page.assert_title_text('Sandbox')
    except NoSuchElementException:
            print("Login Failed")


if __name__ == '__main__':
    unittest.main(verbosity=2)
