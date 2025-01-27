import pytest
import requests
from hamcrest import assert_that, equal_to

from lesson_24_api.conftest import BASE_URL
from lesson_24_api.logger_config import logger


# Є Flask app яке дозволяє робити аутентифiкацию i пiсля цього шукати автомобiлi через GET запрос.
# Потрiбно через Pytest органiзувати тестування даного app використовуючи параметризацiю ( 5-7 наборiв даних )
# з рiзними параметрами GET запиту **sort_by** i **limit**.
# Тест повинен використовувати модуль **request**.
# Первинна аутентифiкация повинна бути органiзована у виглядi фiкстури **scope=’class’**.
# Сам тест повинен вмiти робити логування не тiльки в консоль але i в файл **test_search.log**


def get_all_cars(headers, parameters):
    url = f'{BASE_URL}/cars'
    return requests.get(url=url, headers=headers, params=parameters)


def deserialize_cars(response: requests):
    cars = response.json()
    from lesson_24_api.car_object import Car
    return [Car(**car) for car in cars]


@pytest.mark.parametrize(
    "sort_by,limit,expected_status",
    [
        (None, None, 200),
        ("price", 5, 200),
        ("year", 20, 200),
        ("engine_volume", 3, 200),
        ("brand", None, 200),
        ("invalid_field", 5, 200),
        (None, 0, 200),
    ],
)
def test_get_all_cars(auth_headers, sort_by, limit, expected_status):
    parameters = {'sort_by': sort_by, 'limit': limit}
    response = get_all_cars(auth_headers, parameters)

    logger.info(
        "GET /cars with params: sort_by=%s, limit=%s | Status: %s | Response: %s",
        sort_by,
        limit,
        response.status_code,
        response.json() if response.status_code == 200 else response.text
    )

    assert_that(response.status_code, equal_to(expected_status),
                f"Status code is incorrect. Actual status code is: {response.status_code}")

    cars = deserialize_cars(response)

    if limit is not None:
        assert_that(len(cars), equal_to(limit))

    if sort_by in ["price", "year", "engine_volume", "brand"]:
        values = [getattr(car, sort_by) for car in cars]
        assert_that(values, equal_to(sorted(values)), f'Cars are sorted incorrectly by {sort_by}')
