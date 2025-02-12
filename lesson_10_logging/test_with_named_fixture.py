import os
import re
from datetime import datetime

import pytest

from lesson_10_logging.homework_10 import my_log_event, main_log_file_name, timestamp_pattern


def get_timestamp_by_pattern(pattern, line):
    match = re.search(pattern, line)
    return match.group()


@pytest.mark.parametrize('username, status, log_level', [
    ("Yehor", "success", 'INFO'),
    ("Yehor expired acc", "expired", 'WARNING'),
    ("Unexpected_User", "invalid", 'ERROR')
])
def test_log_event_with_timestamp(username, status, log_level):
    actual_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    my_log_event(username=username, status=status)
    log_filename = main_log_file_name

    with open(log_filename, mode='r') as log_file:
        lines = log_file.readlines()

    last_line = lines[-1].strip()

    expected_time = get_timestamp_by_pattern(timestamp_pattern, last_line)

    expected_line = f"Login event - Username: {username}, Status: {status} - {log_level}"
    # comparing 2 timestamps: from test's start time and from last log line, rounding to seconds
    assert actual_time == expected_time and last_line.endswith(expected_line), "Log message was not as expected."


@pytest.fixture(scope='session')
def cleanup_log_file():
    if os.path.exists(main_log_file_name):
        os.remove(main_log_file_name)
    yield


@pytest.mark.usefixtures("cleanup_log_file")
@pytest.mark.parametrize('username, status, log_level', [
    ("Yehor", "success", 'INFO'),
    ("Yehor expired acc", "expired", 'WARNING'),
    ("Unexpected_User", "invalid", 'ERROR')
])
def test_log_event__with_timestamp(username, status, log_level):
    my_log_event(username=username, status=status)
    log_filename = 'login_system.log'

    with open(log_filename, mode='r') as log_file:
        lines = log_file.readlines()

    last_line = lines[-1].strip()
    expected_line = f"Login event - Username: {username}, Status: {status} - {log_level}"
    assert last_line.endswith(expected_line), "Log message was not as expected."
