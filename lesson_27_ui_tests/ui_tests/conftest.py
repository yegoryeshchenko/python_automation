import pytest
from selenium.webdriver import Chrome, ChromeOptions

from lesson_27_ui_tests.np_tracking.pages.np_tracking_page import NPTrackingPage


@pytest.fixture
def driver():
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    chrome_options.browser_version = "114"
    driver = Chrome(options=chrome_options)
    yield driver
    driver.close()


@pytest.fixture
def np_tracking_page(driver):
    tracking_page = NPTrackingPage(driver)
    tracking_page.open_page()
    return tracking_page
