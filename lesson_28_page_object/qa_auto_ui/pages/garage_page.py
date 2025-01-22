from lesson_28_page_object.qa_auto_ui.locators.garage_page_locators import GaragePageLocators
from lesson_28_page_object.qa_auto_ui.pages.base_page import QAAutoBasePage
from settings import settings


class GaragePage(QAAutoBasePage):
    def __init__(self, driver):
        super().__init__(driver=driver)
        self.url = settings.QAAUTO_BASE_API_URL
        self.locators = GaragePageLocators()

    def open_page(self, url=None):
        url = url or self.url
        self._driver.get(url)

    def _profile_btn(self):
        return self._button(self.locators.profile_button)

    def go_to_user_profile(self):
        self._profile_btn().click()
        return self

    def _profile_name(self):
        return self._present_element(self.locators.user_name)

    def get_profile_name(self):
        return self._profile_name().text