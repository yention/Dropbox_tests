import pytest
from selenium.webdriver.common.by import By

from Config import Locators
from Config.Locators import MainPageLocators
from Config.TestData import TestData
from Pages.BasePage import BasePage
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):

    def __init__(self, driver, url):
        super(BasePage, self).__init__(driver)
        self.page_url = url

    def go_to_sign_in(self):
        self.wait.until(EC.visibility_of_element_located(MainPageLocators.SIGN_IN_LINK)).click()

    def click_to_icon(self):
        self.click_to_btn(MainPageLocators.LOGO_LINK)

    def click_to_plan_n_pricing(self):
        self.click_to_btn(MainPageLocators.PLANS_PRICING_LINK)

    def move_to_why_dropbox(self):
        self.move_to_element(MainPageLocators.WHY_DROPBOX_DROPDOWN)

    def click_dropdown_element(self, element):
        XPATH_element = Locators.DropDownMenu.FRAME + "\'" + str(element) + "\'" + ')]'
        self.click_in_new_tab((By.XPATH, XPATH_element))
