import time

from Config.Locators import MainLogInPage
from Pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver, url):
        super(LoginPage, self).__init__(driver)
        self.page_url = url
        self.go_to_page()

    def enter_invalid_email(self, text):
        self.enter_email(MainLogInPage.EMAIL_FIELD, text)


    def enter_invalid_password(self, text):
        self.enter_password(MainLogInPage.PASSWORD_FIELD, text)

    def enter_valid_email(self, text):
        self.enter_email(MainLogInPage.EMAIL_FIELD, text)

    def enter_valid_password(self, text):
        self.enter_email(MainLogInPage.PASSWORD_FIELD, text)

    def click_to_signin(self):
        self.click_to_btn(MainLogInPage.BUTTON_SIGN_IN)

    def action_for_verification(self):
        # if self.is_element_present(MainLogInPage.VERIFICATION_ALARM):
            # self.click_to_btn(MainLogInPage.VERIFICATION_BTN)
            # time.sleep(10)
        time.sleep(10)
