import pytest


class BaseValues:
    def get_data(self):
        return self.data


class PositiveValues:
    data = [1, 2, 3, 4]

    def get_data(self):
        return self.data


class NegativeValues:
    data = [None, False, '0', {1, 2}]

    def get_data(self):
        return self.data


@pytest.mark.parametrize('value', PositiveValues().get_data())
def test_positive_shos(value):
    pass


@pytest.mark.parametrize('value', NegativeValues().get_data())
def test_negative_shos(value):
    pass

