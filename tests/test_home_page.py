import time
import pytest

from Utils.date_reader import DataReader
from Utils.faker_helper import generate_fake_data
from tests.base_test import BaseTest


class TestHomePage(BaseTest):

    #test should contain assertions (validation)
    @pytest.mark.parametrize("data", DataReader.get_data("home_page_data.json"))
    def test_user_registration_success(self,data):
        self.logger.info("Filling registration form")
        self.home_page.fill_full_form(data)
        self.logger.info("Verifying success message")
        self.verify_equals(self.home_page.success_text(),
                           "Success! The Form has been submitted successfully!.",
                           "Success message did not match")

    @pytest.mark.regression
    def test_print_fake_data(self):
        self.home_page.enter_name(generate_fake_data("first_name"))
        self.home_page.enter_email(generate_fake_data("email"))
        time.sleep(3)



