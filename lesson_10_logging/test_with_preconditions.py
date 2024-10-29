import os

import pytest

from lesson_10_logging.homework_10 import log_event, main_log_file_name


@pytest.fixture(scope='session', autouse=True)
def cleanup_log_file():
    log_filename = main_log_file_name
    if os.path.exists(log_filename):
        os.remove(log_filename)
    yield


@pytest.mark.parametrize('username, status, log_level', [
    ("Yehor", "success", 'INFO'),
    ("Yehor expired acc", "expired", 'WARNING'),
    ("Unexpected_User", "invalid", 'ERROR')
])
def test_log_event__with_timestamp(username, status, log_level):
    log_event(username=username, status=status)
    log_filename = 'login_system.log'

    with open(log_filename, mode='r') as log_file:
        lines = log_file.readlines()

    last_line = lines[-1].strip()
    expected_line = f"Login event - Username: {username}, Status: {status} - {log_level}"
    assert last_line.endswith(expected_line), "Log message was not as expected."