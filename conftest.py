
import pytest
from selenium import webdriver
from utils.screenshot_utils import save_screenshot
from utils.config_reader import ConfigReader
from utils.logger import get_logger
from pages.home_page import HomePage
from pages.shop_page import ShopPage

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
    return request.config.getoption("--browser_name").lower()

@pytest.fixture
def env(request):
    return request.config.getoption("--env").upper()

@pytest.fixture
def headless(request):
    return request.config.getoption("--headless")

# =========================
# Driver Fixture
# =========================
@pytest.fixture
def get_driver(request, browser, env, headless):

    logger = get_logger(__name__)
    driver = None

    if browser== "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless")

        logger.info("Launching Chrome browser")
        driver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("--headless")

        logger.info("Launching Firefox browser")
        driver = webdriver.Firefox(options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    config = ConfigReader(env)
    driver.get(config.get("url"))
    print(config.get("username"))
    print(config.get("password"))

    driver.maximize_window()

    # Page Object injection
    request.cls.home_page = HomePage(driver)
    request.cls.shop_page = ShopPage(driver)

    yield driver

    logger.info("Closing browser")
    driver.quit()