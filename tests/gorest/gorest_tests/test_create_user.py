import pytest
import os


import time  # time.time() - повертає поточний час в секундах

import allure
from dotenv import load_dotenv

from settings import settings
from tests.gorest.dto_user import UserSchema
from tests.gorest.gorest_ctrl import GorestCtrl


@allure.step('Getting static user data')
def get_user_data():
    return {"name": "Tenali Ramakrishna",
                 "gender": "male",
                 "email": f"tenali.ramakrishna@{time.time()}.com",
                 "status": "active"}


@allure.step('Assertation of response')
def validate_data(res):
    UserSchema().load(res, many=True)


@allure.epic('Api tests')
@allure.feature('Gorest')
@allure.story('Creating users')
@allure.title("Create user positive")
@pytest.mark.gorest
def test_create_user():
    user_data = get_user_data()



    # res = GorestCtrl().create_user(data=user_data)
    res = [{"name": "Tenali Ramakrishna",
            "gender": "asd",
            "email": f"tenali.ramakrishna@{time.time()}.com",
            "status": 2,
            "id": 5877}, {"name": "Tenali Ramakrishna",
                          "gender": "asd",
                          "email": f"tenali.ramakrishna@{time.time()}.com",
                          "status": 2,
                          "id": 5877}]

    validate_data(res)


@allure.title("Create user negative")
@pytest.mark.negative
@pytest.mark.gorest
def test_create_user_auth_problem():
    user_data = {"name": "Tenali Ramakrishna",
                 "gender": "male",
                 "email": f"tenali.ramakrishna@{time.time()}.com",
                 "status": "active"}

    GorestCtrl().create_user(data=user_data, token='asd', status_code=401)


@pytest.mark.negative
@pytest.mark.gorest
def test_create_for_checking_user_email_at_prod():
    load_dotenv()
    assert  settings.USER_EMAIL == 'test+prod@test.com'
    assert os.getenv('SECRET_PHRASE', None) == 'secret'


