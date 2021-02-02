from actions import Actions
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Config import Locators
from Config.Locators import MainLogInPage
from Pages.Page import Page


class BasePage(Page):

    def __init__(self, driver):
        super(BasePage, self).__init__(driver)
        self.page_url = str()

    def should_be_in_url(self, part_of_url):
        assert part_of_url in self.driver.current_url, 'URL is wrong'

    def click_to_btn(self, element):
        if self.is_element_available(element):
            self.driver.find_element(*element).click()

    def enter_email(self, element, text):
        self.wait.until(EC.visibility_of_element_located(element)).send_keys(text)

    def enter_password(self, element, text):
        self.wait.until(EC.visibility_of_element_located(element)).send_keys(text)

    def go_to_page(self):
        self.driver.get(self.page_url)


    #useless already
    # def click_in_new_tab(self, element):
    #     if self.is_element_available(element):
    #         self.driver.current_window_handle
    #         self.driver.find_element(*element).send_keys(Keys.CONTROL + Keys.RETURN)
    #         self.driver.switch_to.window(self.driver.window_handles[1])

