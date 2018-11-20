from locators.weblocators import WebLocators as loc


class LoginPage:

    def __init__(self, context):
        self.driver = context

    def enter_username(self, username):
        self.driver.find_by_id(loc.username_editbox_id).clear()
        self.driver.find_by_id(loc.username_editbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_by_id(loc.password_editbox_id).clear()
        self.driver.find_by_id(loc.password_editbox_id).send_keys(password)

    def click_signin(self):
        self.driver.find_by_id(loc.login_button_id).click()
