import allure
import pytest
from hamcrest import assert_that


# @allure.feature("Nova Poshta")
# @pytest.mark.ui_tests
def test_track_package(driver, np_tracking_page):

    np_tracking_page.open_page()
    np_tracking_page.search_parcel()

    expected_error_message = ('Ми не знайшли посилку за таким номером. Якщо ви шукаєте інформацію про посилку, '
                              'якій більше 3 місяців, будь ласка, зверніться у контакт-центр: 0 800 500 609')
    actual_error_message = np_tracking_page.get_error_message_text()
    assert_that(actual_error_message, expected_error_message, "Error message does not match!")

