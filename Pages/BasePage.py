from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Config import Locators
from Pages.Page import Page


class BasePage(Page):

    def __init__(self, driver):
        super(BasePage, self).__init__(driver)
        self.page_url = str()

    def open_page(self):
        self.driver.get(self.page_url)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except NoSuchElementException:
            return False
        return True


    def is_element_available(self, how, what):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((how, what))
            )
        except:
            return False
        return True

    def should_be_url(self, part_of_url):
        assert part_of_url in self.driver.current_url, 'URL is wrong'
