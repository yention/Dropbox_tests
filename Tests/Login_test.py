import pytest

from Config.Locators import MainLogInPage
from Config.TestData import TestData
from Pages.LoginPage import LoginPage


class TestLoginPage():

    @pytest.mark.parametrize('invalid_email', TestData.ACCOUNT_INVALID_DATES['email'])
    def test_invalid_login(self, invalid_email):
        self.page = LoginPage(self.driver, TestData.LOGIN_PAGE['url'])
        self.page.enter_invalid_email(invalid_email)
        self.page.enter_valid_password(TestData.ACCOUNT_DATES['password'])
        self.page.click_to_signin()
        self.page.action_for_verification()
        assert self.page.is_element_present(MainLogInPage.NOTICE_WRONG_DATES) == True


    @pytest.mark.parametrize('invalid_password', TestData.ACCOUNT_INVALID_DATES['password'])
    def test_invalid_password(self, invalid_password):
        self.page = LoginPage(self.driver, TestData.LOGIN_PAGE['url'])
        self.page.enter_valid_email(TestData.ACCOUNT_DATES['email'])
        self.page.enter_invalid_password(invalid_password)
        self.page.click_to_signin()
        self.page.action_for_verification()
        assert self.page.is_element_present(MainLogInPage.NOTICE_WRONG_DATES) == True
