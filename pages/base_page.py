import logging

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
# reusable selenium wrappers

class BasePage():

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = logging.getLogger(self.__class__.__name__)

    def open_url(self, url):
        self.logger.info(f"Opening URL: {url}")
        self.driver.get(url)

    def find_element(self, locator):
        self.logger.info(f"Finding element: {locator}")
        return self.wait.until(EC.visibility_of_element_located(locator))

    def send_keys(self, locator, text):
        self.logger.info(f"Typing into element {locator}: {text}")
        self.find_element(locator).send_keys(text)

    def click(self, locator):
        self.logger.info(f"Clicking element: {locator}")
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def select_dropdown_value(self, locator, value):
        self.logger.info(f"Selecting dropdown value: {value}")
        dropdown = Select(self.find_element(locator))
        dropdown.select_by_visible_text(value)

    def get_text(self, locator):
        text = self.find_element(locator).text
        self.logger.info(f"Getting text from {locator}: {text}")
        return text

    def find_multiple_elements(self, locator):
        self.logger.info(f"Finding multiple elements: {locator}")
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def get_count_elements(self, locator):
        count = len(self.find_multiple_elements(locator))
        self.logger.info(f"Count of elements {locator}: {count}")
        return count

    def is_displayed(self, locator):
        result = self.find_element(locator).is_displayed()
        self.logger.info(f"Element displayed {locator}: {result}")
        return result

    def get_url(self):
        url = self.driver.current_url
        self.logger.info(f"Current URL: {url}")
        return url

    #click(), send_keys(), find_element(), select_dropdown_value() == Abstraction methods