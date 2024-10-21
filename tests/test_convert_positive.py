import pytest

from test_functions import convert_to_24_hour


@pytest.mark.convert
class TestConvertAMPositive:

    @pytest.mark.parametrize('input_value,expected_result', [
        ('10:22 AM', '10:22'),
        pytest.param('1:34 AM', '01:34'),
        pytest.param('1:34 AM', '01:34', marks=pytest.mark.xfail(reason='known issue xfail')),
        pytest.param('1:34 AM', '01:34', marks=pytest.mark.skipif(reason='Only for dev')),
        pytest.param('1:34 AM', '01:34', marks=pytest.mark.exp),
        ('00:01 AM', '00:01')
    ])
    def test_convert_am_hours_parametrized(self, input_value, expected_result):
        assert convert_to_24_hour(input_value) == expected_result

    my_string = 'asd'

    @pytest.mark.parametrize('input_value', my_string)
    def test_convert_am_hours_10_22(self, input_value):
        assert 'input_value' == 'a'

    @pytest.mark.convert
    def test_convert_am_hours_1_34(self):
        assert convert_to_24_hour('1:34 AM') == '01:34'

    @pytest.mark.convert
    def test_convert_am_hours_00_01(self):
        assert convert_to_24_hour('00:01 AM') == '00:01'
