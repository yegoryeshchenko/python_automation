import allure

from lesson_28_page_object.qa_auto_ui.dtos.user_dto import UserDTO
from lesson_28_page_object.qa_auto_ui.locators.registration_page_locators import RegistrationPageLocators
from lesson_28_page_object.qa_auto_ui.pages.base_page import QAAutoBasePage
from lesson_28_page_object.qa_auto_ui.pages.garage_page import GaragePage


class RegistrationPage(QAAutoBasePage):
    def __init__(self, driver):
        super().__init__(driver=driver)
        self.locators = RegistrationPageLocators()

    def open_page(self, url=None):
        url = url or self.url
        self._driver.get(url)

    def _first_name(self):
        return self._present_element(self.locators.first_name, 'First name field is not present')

    def _last_name(self):
        return self._present_element(self.locators.last_name, 'Last name field is not present')

    def _signup_email(self):
        return self._present_element(self.locators.signup_email, 'Signup email field is not present')

    def _signup_password(self):
        return self._present_element(self.locators.signup_password, 'Signup password field is not present')

    def _repeat_signup_password(self):
        return self._present_element(self.locators.signup_repeat_password, 'Re-enter signup password field '
                                                                           'is not present')

    def _register_button(self):
        return self._button(self.locators.register_button, 'Register button is not displayed')

    def set_first_name(self, first_name):
        self._first_name().send_keys(first_name)
        return self

    def set_last_name(self, last_name):
        self._last_name().send_keys(last_name)
        return self

    def set_signup_email(self, email):
        self._signup_email().send_keys(email)
        return self

    def set_password(self, usr_password):
        self._signup_password().send_keys(usr_password)
        return self

    def set_repeat_password(self, usr_password):
        self._repeat_signup_password().send_keys(usr_password)
        return self

    def click_register_button(self):
        self._register_button().click()
        return self

    @allure.step("register new user")
    def register_user(self, user: UserDTO):
        self.set_first_name(user.first_name).set_last_name(user.last_name).set_signup_email(user.email).set_password(
            user.password).set_repeat_password(user.password)
        self.click_register_button()
        return GaragePage(self._driver)
