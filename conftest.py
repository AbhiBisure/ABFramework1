from pathlib import Path
import pytest
from pygments.styles import default
from selenium import webdriver

import settings
from Utils.logger import get_logger
from pages.home_page import HomePage

logger = get_logger()

def pytest_addoption(parser):
    parser.addoption("--browser",default="chrome")
    parser.addoption("--headless",action="store_true")
    parser.addoption("--env",default="QA")

@pytest.fixture()
def get_browser(request):
    browser=request.config.getoption("--browser")
    return browser

@pytest.fixture()
def get_env(request):
    env=request.config.getoption("--env")
    return env

@pytest.fixture()
def is_headless(request):
    return request.config.getoption("--headless")

@pytest.fixture()
def get_driver(request,get_browser,get_env,is_headless):
    global driver
    if get_browser.lower() == "chrome":
        chrome_options = webdriver.ChromeOptions()
        if is_headless:
            chrome_options.add_argument("--headless")
        logger.info("Launching Chrome Browser")
        driver = webdriver.Chrome(options=chrome_options)
    elif get_browser.lower() == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        if is_headless:
            firefox_options.add_argument("-headless")
        logger.info("Launching Firefox Browser")
        driver = webdriver.Firefox(options=firefox_options)
    else:
        print(f"Browser'{get_browser}' is not supported.")
        #raise ValueError(
        #    f"Browser '{get_browser}' is not supported"
        #)
    if get_env.upper() == "QA":
        driver.get(settings.QA_URL)
    elif get_env.upper() == "UAT":
        driver.get(settings.UAT_URL)

    driver.implicitly_wait(10)
    driver.maximize_window()
#    request.cls.driver = driver
    request.cls.home_page = HomePage(driver)
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs['get_driver']
        screenshot_dir = Path("screenshots")
        screenshot_dir.mkdir(exist_ok=True)
        screenshot_file = screenshot_dir / f"{item.name}.png"
        driver.save_screenshot(str(screenshot_file))
        print(f"Screenshot saved to {screenshot_file}")