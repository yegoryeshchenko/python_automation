import pytest
from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

from lesson_28_page_object.qa_auto_ui.dtos.user_dto import UserDTO
from lesson_28_page_object.qa_auto_ui.pages.garage_page import GaragePage
from lesson_28_page_object.qa_auto_ui.pages.login_page import LoginPage
from lesson_28_page_object.qa_auto_ui.pages.main_page import MainPage
from lesson_28_page_object.qa_auto_ui.pages.registration_page import RegistrationPage


@pytest.fixture(scope='session')
def driver():
    chrome_options = ChromeOptions()

    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--no-sandbox")  # Required for Jenkins
    chrome_options.add_argument("--disable-dev-shm-usage")  # Prevent crashes
    chrome_options.add_argument("--disable-gpu")  # Fixes GPU-related issues
    chrome_options.add_argument("--remote-debugging-port=9222")  # Debugging

    service = ChromeService(ChromeDriverManager().install()) 

    driver = webdriver.Chrome(service=service, options=chrome_options)

    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def test_user():
    faker = Faker()
    first_name = faker.first_name()
    last_name = faker.last_name()
    email = faker.email()
    password = faker.password()
    user = UserDTO(first_name, last_name, email, password)
    yield user


@pytest.fixture(scope='session')
def main_page(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    return main_page


@pytest.fixture(scope='session')
def login_page(driver):
    login_page = LoginPage(driver)
    return login_page


@pytest.fixture(scope='session')
def registration_page(driver):
    registration_page = RegistrationPage(driver)
    return registration_page


@pytest.fixture(scope='session')
def garage_page(driver):
    garage_page = GaragePage(driver)
    return garage_page
