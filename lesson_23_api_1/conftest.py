import faker
import pytest
from faker import Faker


@pytest.fixture(scope='module')
def base_url():
    print('Calling base url fixture')
    yield 'http://127.0.0.1:8080'



