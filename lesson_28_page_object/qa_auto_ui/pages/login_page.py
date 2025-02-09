import allure

from lesson_28_page_object.qa_auto_ui.locators.login_page_locators import LoginPageLocators
from lesson_28_page_object.qa_auto_ui.pages.base_page import QAAutoBasePage
from lesson_28_page_object.qa_auto_ui.pages.registration_page import RegistrationPage


class LoginPage(QAAutoBasePage):
    def __init__(self, driver):
        super().__init__(driver=driver)
        self.locators = LoginPageLocators()

    def open_page(self, url=None):
        url = url or self.url
        self._driver.get(url)

    def _registration_button(self):
        return self._button(self.locators.registration_button, 'Registration button is not displayed!')

    @allure.step("click on registration button")
    def click_on_registration_button(self):
        self._registration_button().click()
        return RegistrationPage(self._driver)
