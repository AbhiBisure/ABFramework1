from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from Utils.logger import get_logger
# reusable selenium wrappers
class BasePage:

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)
        self.logger = get_logger()

    def open_url(self,url):
        self.logger.info(f"Opening URL: {url}")
        self.driver.get(url)

    def find_element(self,locator):
        return self.wait.until(expected_conditions.visibility_of_element_located(locator))
    #it executes the explicit wait until the element is visible. As soon as it appears wait block returns WebElement

    def send_keys(self,locator,text):
        self.find_element(locator).send_keys(text)

    def click(self, locator):
        self.logger.info(f"Clicking on {locator}")
        self.wait.until(expected_conditions.element_to_be_clickable(locator)).click()

    def select_dropdown_value(self,locator,gender):
        dropdown= Select(self.find_element(locator))
        dropdown.select_by_visible_text(gender)

    def get_text(self,locator):
        return self.find_element(locator).text

    def find_multiple_elements(self, locator):
        return self.wait.until(expected_conditions.visibility_of_all_elements_located(locator))

    def get_count_elements(self, locator):
        return len(self.find_multiple_elements(locator))

    def is_displayed(self, locator):
        return self.find_element(locator).is_displayed()

    # click(), send_keys(), find_element(), select_dropdown_value() == Abstraction methods