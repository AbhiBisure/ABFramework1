import pytest
import settings
from tests.base_test import BaseTest
from data.data_reader import DataReader

class TestHomePage(BaseTest):

    #test should contain assertions (validation)
    @pytest.mark.parametrize("data", DataReader.get_data("home_page_data.json"))
    def test_user_registration_success(self,data):
        self.home_page.fill_full_form(data)
        actual = self.home_page.success_text()
        assert "Success!" in actual
