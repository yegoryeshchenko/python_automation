import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

from lesson_27_ui_tests.np_tracking.pages.np_tracking_page import NPTrackingPage


@pytest.fixture
def driver():
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--headless")  # Run tests in headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Automatically install the correct ChromeDriver version
    service = ChromeService(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=chrome_options)

    yield driver
    driver.quit()


@pytest.fixture
def np_tracking_page(driver):
    tracking_page = NPTrackingPage(driver)
    tracking_page.open_page()
    return tracking_page
