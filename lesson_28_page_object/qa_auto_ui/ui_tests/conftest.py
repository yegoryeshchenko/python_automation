import pytest
from faker import Faker
from selenium.webdriver import Chrome, ChromeOptions

from lesson_28_page_object.qa_auto_ui.dtos.user_dto import UserDTO
from lesson_28_page_object.qa_auto_ui.pages.garage_page import GaragePage
from lesson_28_page_object.qa_auto_ui.pages.login_page import LoginPage
from lesson_28_page_object.qa_auto_ui.pages.main_page import MainPage
from lesson_28_page_object.qa_auto_ui.pages.registration_page import RegistrationPage


@pytest.fixture(scope='session')
def driver():
    chrome_options = ChromeOptions()
    # chrome_options.add_argument("--headless") # test fails with timeout if running in headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    chrome_options.browser_version = "114"
    driver = Chrome(options=chrome_options)
    yield driver
    driver.close()

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
