from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def is_element_present(self, element):
        try:
            self.wait.until(
                EC.presence_of_element_located(element)
            )
        except:
            return False
        return True

    def get_presents_element(self, element):
        if self.is_element_present(element):
            return element
        else:
            None

    def is_element_available(self, element):
        try:
            self.wait.until(
                EC.element_to_be_clickable(element)
            )
        except:
            return False
        return True

    def move_to_element(self, element):
        if self.is_element_available(element):
            target = self.get_presents_element(element)
            actions = ActionChains(self.driver)
            actions.move_to_element(target).perform()
