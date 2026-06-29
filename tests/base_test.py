import pytest
from utils.logger import get_logger

@pytest.mark.usefixtures("get_driver")
class BaseTest:

    def setup_method(self, method):
        self.logger = get_logger(self.__class__.__name__)
        self.logger.info(f"STARTING TEST: {method.__name__}")

    def teardown_method(self, method):
        self.logger.info(f"FINISHED TEST: {method.__name__}")

    def verify_equals(self, actual, expected, message=""):
        assert actual == expected,f"{message}\nExpected: {expected}\nActual: {actual}"
        #check.equal(actual, expected, f"{message} (Expected: {expected}, Actual: {actual})")

    def verify_not_equals(self, actual, expected, message=""):
        assert actual != expected,f"{message}\nExpected actual value to not equal: {expected}"

    def verify_contains(self, actual, expected, message=""):
        assert expected in actual,f"{message}\n'{expected}' not found in '{actual}'"
        #check.is_in(expected, actual, f"{message}")

    def verify_true(self, condition, message=""):
        assert condition is True, f"{message}\nExpected condition to be True, but got: {condition}"
        #check.is_true(condition, f"{message}")

    def verify_false(self, condition, message=""):
        assert condition is False,f"{message}\nExpected condition to be False, but got: {condition}"

    def verify_empty(self, actual, message=""):
        assert len(actual) == 0,f"{message}\nExpected container to be empty, but it has {len(actual)} items"
        #check.is_none(actual, f"{message}")

    def verify_not_empty(self, actual, message=""):
        assert len(actual) > 0,f"{message}\nExpected container to not be empty"

    # --- Numeric Ranges ---
    def verify_greater(self, actual, threshold, message=""):
        assert actual > threshold,f"{message}\nExpected '{actual}' to be greater than '{threshold}'"
        #check.greater(actual, threshold, f"{message}")

    def verify_less(self, actual, threshold, message=""):
        assert actual < threshold,f"{message}\nExpected '{actual}' to be less than '{threshold}'"
        #check.less(actual, threshold, f"{message}")

    def verify_between(self, actual, low, high, message=""):
        assert low <= actual <= high,f"{message}\nExpected '{actual}' to be between '{low}' and '{high}'"
        #check.is_true(low <= actual <= high, f"{message} (Expected {actual} to be between {low} and {high})")

# pytest automatically shows detailed differences when an assertion fails.
# If you keep wrapper methods, ensure they add value—such as consistent logging, screenshots on failure,
# or standardized error messages—rather than simply wrapping assert.