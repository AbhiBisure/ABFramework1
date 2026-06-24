import logging
import pytest

@pytest.mark.usefixtures("get_driver")
class BaseTest:

    def setup_method(self, method):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.info(f"STARTING TEST: {method.__name__}")

    def teardown_method(self, method):
        self.logger.info(f"FINISHED TEST: {method.__name__}")

    def verify_equals(self, actual, expected, message=""):
        assert actual == expected, (
            f"{message}\nExpected: {expected}\nActual: {actual}"
        )

    def verify_contains(self, actual, expected, message=""):
        assert expected in actual, (
            f"{message}\n'{expected}' not found in '{actual}'"
        )