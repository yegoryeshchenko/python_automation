import pytest
import requests

BASE_URL = 'http://127.0.0.1:8080'


@pytest.fixture(scope='session')
def auth_headers():
    response = (requests.post(f'{BASE_URL}/auth',
                              auth=requests.auth.HTTPBasicAuth(username='test_user', password='test_pass')))
    token = response.json().get("access_token")

    return {"Authorization": f"Bearer {token}"}
