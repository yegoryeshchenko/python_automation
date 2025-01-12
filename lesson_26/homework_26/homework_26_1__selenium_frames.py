from time import sleep

import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

BASE_URL = "http://localhost:8000/dz.html"


def type_into_field_with_id_and_click_check_btn(field_id, text):
    driver.find_element(By.ID, field_id).send_keys(text)
    # можемо не уточнювати селектор для button, тому що він один на фрейм
    driver.find_element(By.XPATH, "//button").click()


def switch_to_frame(frame_id: str):
    driver.switch_to.frame(frame_id)


def check_that_alert_message_text_equals_to(alert_message):
    assert driver.switch_to.alert.text == alert_message


def accept_alert():
    driver.switch_to.alert.accept()


@pytest.fixture(scope="function", autouse=True)
def setup_and_teardown():
    global driver
    driver = WebDriver()
    yield
    driver.quit()


@pytest.mark.parametrize('frame_id, input_id, secret_word', [
    ('frame1', 'input1', 'Frame1_Secret'),
    ('frame2', 'input2', 'Frame2_Secret'),
])
def test_check_that_secret_word_is_correct(frame_id, input_id, secret_word):
    driver.get(BASE_URL)
    switch_to_frame(frame_id)
    type_into_field_with_id_and_click_check_btn(input_id, secret_word)
    # залишив sleep() для наглядності
    sleep(1)
    check_that_alert_message_text_equals_to("Верифікація пройшла успішно!")
    sleep(1)
    accept_alert()
    sleep(1)
