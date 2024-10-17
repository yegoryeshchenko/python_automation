# custom exceptions
import random


class RoiErrors(Exception):
    def __init__(self, message):
        super().__init__(message)


def get_data_from_db(company_id):
    return [company_id, f'Google {company_id}', random.random()]


def test_check_company():
    db_data = get_data_from_db(20)

    if db_data[2] <= 0.8:
        raise RoiErrors('Roi Data < 0.8')
