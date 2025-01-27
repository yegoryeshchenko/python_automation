import allure

from lesson_28_page_object.qa_auto_ui.locators.main_page_locators import MainPageLocators
from lesson_28_page_object.qa_auto_ui.pages.base_page import QAAutoBasePage
from lesson_28_page_object.qa_auto_ui.pages.login_page import LoginPage
from settings import settings


class MainPage(QAAutoBasePage):

    def __init__(self, driver):
        super().__init__(driver=driver)
        # self.url = settings.QAAUTO_BASE_API_URL
        self.url = "https://guest:welcome2qauto@qauto2.forstudy.space"
        self.locators = MainPageLocators()

    @allure.step("open QA Auto main page")
    def open_page(self, url=None):
        url = url or self.url
        self._driver.get(url)

    def _sign_in_button(self):
        return self._button(self.locators.sign_in_button, 'Sign button is not displaying!')

    @allure.step("click on sign in button")
    def click_on_sign_in_button(self):
        self._sign_in_button().click()
        return LoginPage(self._driver)
