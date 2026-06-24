
import pytest
import logging
from selenium import webdriver
from Utils.screenshot_utils import save_screenshot
from Utils.config_reader import ConfigReader
from pages.home_page import HomePage
from pages.shop_page import ShopPage

# =========================
# Logging Configuration
# =========================
logging.basicConfig(
    filename="automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# =========================
# Screenshot Hook
# =========================
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs['get_driver']
        if driver:
            path = save_screenshot(driver, item.name)
            print(f" Screenshot saved to {path}")

# =========================
# CLI Options
# =========================
def pytest_addoption(parser):
    parser.addoption("--browser_name", default="chrome")
    parser.addoption("--headless", action="store_true")
    parser.addoption("--env", default="QA")

# =========================
# Fixtures
# =========================
@pytest.fixture
def browser(request):
    return request.config.getoption("--browser_name")

@pytest.fixture
def env(request):
    return request.config.getoption("--env")

@pytest.fixture
def headless(request):
    return request.config.getoption("--headless")

# =========================
# Driver Fixture
# =========================
@pytest.fixture
def get_driver(request, browser, env, headless):

    logger = logging.getLogger(__name__)
    # STEP 1: Read config based on environment
    config = ConfigReader(env)
    driver = None

    if browser.lower() == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless")

        logger.info("Launching Chrome browser")
        driver = webdriver.Chrome(options=options)

    elif browser.lower() == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("--headless")

        logger.info("Launching Firefox browser")
        driver = webdriver.Firefox(options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    # Environment selection
    url = config.get("url")
    logger.info(f"Opening URL: {url}")
    driver.get(url)

    driver.maximize_window()
    driver.implicitly_wait(10)

    # Page Object injection
    request.cls.home_page = HomePage(driver)
    request.cls.shop_page = ShopPage(driver)

    yield driver

    logger.info("Closing browser")
    driver.quit()