from Config.Locators import MainLogInPage as LoginLoc, MainLogInPage, AccountDates
from Pages.BasePage import BasePage
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):

    def __init__(self, driver, url):
        super(LoginPage, self).__init__(driver)
        self.page_url = url


