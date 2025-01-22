from selenium.webdriver.common.by import By

class GaragePageLocators:
    profile_button = (By.CSS_SELECTOR, "a[routerlink='profile']")
    user_name = (By.CSS_SELECTOR, "p[class='profile_name display-4']")
