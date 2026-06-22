from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ShopPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    SHOP_LINK = (By.LINK_TEXT, "Shop")

    def navigate_to_shop_page(self):
        self.click(self.SHOP_LINK)
