from random import randint

from lesson_27_ui_tests.np_tracking.locators.np_tracking_locators import NovaPoshtaTrackingLocators
from lesson_27_ui_tests.np_tracking.pages.base_page import BasePage


class NPTrackingPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver=driver)
        self.locators = NovaPoshtaTrackingLocators
        # self.url = settings.nova_poshta_url
        self.url = 'https://tracking.novaposhta.ua'

    def open_page(self, url=None):
        url = url or self.url
        self._driver.get(url)

    @staticmethod
    def generate_tracking_number():
        return ''.join(str(randint(0, 9)) for _ in range(11))

    def _tracking_number_input(self):
        return self._input_field(self.locators.package_tracking_input)

    def type_tracking_number(self, tracking_number):
        self._tracking_number_input().send_keys(tracking_number)
        return self

    def _search_button(self):
        return self._button(self.locators.search_button, message='Cant find Search button at NP Tracking Page',
                            timeout=4)

    def _error_message(self):
        return self._present_element(self.locators.error_message)

    def click_on_search_tracking_number(self):
        self._search_button().click()

    def get_error_message_text(self):
        return self._error_message().text

    def search_parcel(self):
        tracking_number = self.generate_tracking_number()
        print(self.generate_tracking_number())
        self.type_tracking_number(tracking_number).click_on_search_tracking_number()
        return self
