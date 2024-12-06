import logging
from datetime import datetime

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s\n',
                    handlers=[
                        logging.FileHandler('hb_test.log', mode='w')
                    ])


def get_list_of_rows_from_txt(txt_file_path):
    rows = []
    with open(txt_file_path, 'r') as txt_reader:
        for row in txt_reader:
            rows.append(row.strip())

        return rows


def filter_log_by_key(source_log_file, key: str) -> list:
    unfiltered_log = get_list_of_rows_from_txt(source_log_file)
    filtered_log = []

    for row in unfiltered_log:
        if key in row:
            filtered_log.append(row)
    return filtered_log


def get_datetime(row: str) -> datetime:
    row = row.strip()
    date_time = ''
    if 'Timestamp' in row:
        parts = row.split(' ')
        for i, part in enumerate(parts):
            if part == 'Timestamp':
                time_str = parts[i + 1]
                try:
                    date_time = datetime.strptime(time_str, "%H:%M:%S").time()
                except ValueError as value_error:
                    print(f'Error {value_error} occurred when parsing time {time_str}')
    return date_time


def get_seconds_from_time(date_time: datetime):
    return date_time.hour * 3600 + date_time.minute * 60 + date_time.second


def get_time_diff(date_time_1: datetime, date_time_2: datetime):
    seconds_1 = get_seconds_from_time(date_time_1)
    seconds_2 = get_seconds_from_time(date_time_2)
    time_diff = seconds_2 - seconds_1
    return time_diff


def analyze_hart_beat(log_file, filter_key):
    list_to_analyze = filter_log_by_key(log_file, filter_key)

    for k, row in enumerate(list_to_analyze[:-1]):
        date_time_1 = get_datetime(row)
        date_time_2 = get_datetime(list_to_analyze[k + 1])
        time_diff = get_time_diff(date_time_2, date_time_1)
        if 31 < time_diff < 33:
            warning_message = (f"WARNING: Pay attention to rows:\n{list_to_analyze[k + 1]}\n"
                               f"{list_to_analyze[k]}\n"
                               f"Time difference: {time_diff} seconds\nHappened at: {date_time_1.strftime('%H:%M:%S')}")
            logging.warning(warning_message)
        if time_diff >= 33:
            error_message = (f"ERROR: Heartbeat time difference exceeded threshold:\n"
                             f"{list_to_analyze[k + 1]}\n{list_to_analyze[k]}\n"
                             f"Time difference: {time_diff} seconds\nHappened at: {date_time_1.strftime('%H:%M:%S')}")
            logging.error(error_message)


analyze_hart_beat("hblog.txt", "Key TSTFEED0300|7E3E|0400")
