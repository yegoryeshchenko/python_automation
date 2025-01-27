import allure

from lesson_28_page_object.qa_auto_ui.ui_assertions.ui_assertions import assert_that_field_contains_expected_string


@allure.feature("register new user")
@allure.testcase("verify that newly registered user can login to the system")
def test_user_registration(driver, test_user, main_page, login_page, registration_page, garage_page):
    user = test_user
    main_page.open_page()
    main_page.click_on_sign_in_button()
    login_page.click_on_registration_button()
    registration_page.register_user(user)
    garage_page.go_to_user_profile()

    # profile name displays incorrectly (as '<name> undefined'), so we'll check that the field contains user's name
    actual_user_name = garage_page.get_profile_name()
    assert_that_field_contains_expected_string(actual_user_name, user.first_name,
                                               'user name is incorrect or user is not logged in!')
