from selenium.webdriver.common.by import By


class NovaPoshtaTrackingLocators:
    package_tracking_input = (By.CSS_SELECTOR, 'input.track__form-group-input')
    search_button = (By.ID, 'np-number-input-desktop-btn-search-en')
    error_message = (By.ID, 'np-number-input-desktop-message-error-message')
