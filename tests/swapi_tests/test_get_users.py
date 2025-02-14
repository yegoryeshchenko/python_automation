import allure
import pytest

from tests.swapi_tests.swapi_ctrl import SwapiCtrl

swapi_ctrl = SwapiCtrl()

@allure.epic('Api tests')
@pytest.mark.swapi
@allure.description('swapi user tests, just create user')
def test_get_users():

    response = swapi_ctrl.get_people()

    assert response.status_code == 200, f'Expected status code 200, but actual is {response.status_code}'

@allure.epic('Api tests')
@allure.feature('Swapi')
@pytest.mark.xfail(reason='jira_link')
@pytest.mark.swapi
@pytest.mark.parametrize('page_number', [1,2,5, 10])
@allure.link('jira_link')
def test_get_users_with_pages(page_number):

    response = swapi_ctrl.get_people(params={'page': page_number})

    response_data = response.json()  # взяти відповіьв  форматі json
    next_page_value = response_data['next']
    last_number = next_page_value.split('=')[-1]  # ['https://swapi.dev/api/people/?page', '2']

    assert int(last_number) == page_number+1

    #     "count": 82,
    #     "next": "https://swapi.dev/api/people/?page=2",
    #     "previous": null,


@pytest.mark.swapi
@allure.link('jira_tiket/123')
def test_get_users_negative_case_pages():

    swapi_ctrl.get_people(params={'page': 10500}, status_code=404)
