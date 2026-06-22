import time
from tests.base_test import BaseTest

class TestShopTest(BaseTest):

    def test_navigate_to_shop_page(self):
        self.shop_page.navigate_to_shop_page()
        url=self.shop_page.get_url()
        print(url)
        assert url == "https://rahulshettyacademy.com/angularpractice/shop"