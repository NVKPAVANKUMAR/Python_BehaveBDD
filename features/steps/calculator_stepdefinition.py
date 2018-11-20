from behave import given, when, then
from selenium import webdriver
import configparser

from pages.login import LoginPage
from pages.dashboard import DashboardPage
import unittest


def parse_config(header, parameter):
    config = configparser.ConfigParser()
    config.read('configuration/config.ini')
    return config.get(header, parameter)


@given('user is on loginpage')
def navigate_login_page(context):
    context.browser.visit(parse_config('Credentials', 'url'))


@when('user enters valid username and password')
def enter_credentials(context):
    login_page = LoginPage(context.browser)
    login_page.enter_username(parse_config('Credentials', 'username'))
    login_page.enter_password(parse_config('Credentials', 'password'))


@when(u'clicks on login button')
def step_impl(context):
    login_page = LoginPage(context.browser)
    login_page.click_signin()


@then(u'user navigates to dashboardpage')
def step_impl(context):
    dashboard_page = DashboardPage(context.browser)
    dashboard_page.assert_title_text('Corso Moodle')


if __name__ == '__main__':
    unittest.main(verbosity=2)
