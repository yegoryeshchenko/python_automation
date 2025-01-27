from selenium.webdriver.common.by import By

class RegistrationPageLocators:
    first_name = (By.ID, 'signupName')
    last_name = (By.ID, 'signupLastName')
    signup_email = (By.ID, 'signupEmail')
    signup_password = (By.ID, 'signupPassword')
    signup_repeat_password = (By.ID, 'signupRepeatPassword')
    register_button = (By.CSS_SELECTOR, 'div.modal-footer > button')
