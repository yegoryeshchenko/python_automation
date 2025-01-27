from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class QAAutoBasePage:

    def __init__(self, driver):
        self._driver = driver
        self.url = None

    def open_page(self, url=None):
        url = url or self.url
        self._driver.get.url(url)

    def _input_field(self, locator, message='', timeout=3):  # locator = tuple(type_of_selector, selector)
        return WebDriverWait(self._driver, timeout).until(
            EC.presence_of_element_located(locator), message=message)

    def _present_element(self, locator, message='', timeout=3):  # locator = tuple(type_of_selector, selector)
        return WebDriverWait(self._driver, timeout).until(
            EC.presence_of_element_located(locator), message=message)

    def _button(self, locator, message='', timeout=3):  # locator = tuple(type_of_selector, selector)
        return WebDriverWait(self._driver, timeout).until(
            EC.element_to_be_clickable(locator), message=message)
