import allure
from hamcrest import assert_that, contains_string


@allure.step("check that user profile view contains correct user name")
def assert_that_field_contains_expected_string(actual_string, expected_string, error_message):
    assert_that(actual_string, contains_string(expected_string), error_message)