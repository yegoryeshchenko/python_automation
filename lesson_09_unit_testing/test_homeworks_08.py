import pytest

from homeworks import calculate_perimeter, find_all_occurrences_of_a_symbol, number_of_words_with_title_letter, \
    sum_numberz, revert_line


class TestHomeworks:

    # calculate perimeter
    def test_should_calculate_perimeter(self):
        assert calculate_perimeter(1, 2, 3, 4) == 10

    @pytest.mark.parametrize('side_1, side_2, side_3, side_4, expected_result', [
        (1, 2, 3, 4, 10),
        pytest.param(1, 2, 3, 4, 11, marks=pytest.mark.skipif(True, reason='Only for dev')),
        pytest.param(1, 2, 3, 4, 12, marks=pytest.mark.xfail(reason='known issue xfail'))
    ])
    def test_should_calculate_perimeter_parametrized(self, side_1, side_2, side_3, side_4, expected_result):
        assert calculate_perimeter(side_1, side_2, side_3, side_4) == expected_result

    def test_should_fail_when_one_of_arguments_is_zero(self):
        assert calculate_perimeter(1, 2, 3, 0) == 'Усі сторони повинні бути додатними значеннями більше нуля.'

    @pytest.mark.xfail(reason='one of the parameters has a wrong type')
    def test_should_fail_with_wrong_argument(self):
        assert calculate_perimeter(1, 2, 3, '1') == 7

    # find all occurrences

    def test_should_find_all_occurrences(self):
        my_string = "Would you tell ' dMe, sfplease,as dWhifcd'sfgh wayf I oug'fHstf to gosdf fwer'orwm here?"
        assert find_all_occurrences_of_a_symbol(my_string, "'") == ["'", "'", "'", "'"]

    def test_should_return_empty_list_for_empty_string(self):
        my_string = "Would you tell ' dMe, sfplease,as dWhifcd'sfgh wayf I oug'fHstf to gosdf fwer'orwm here?"
        assert find_all_occurrences_of_a_symbol(my_string, "") == []

    # number of words with title letter
    def test_find_number_of_words_with_title_letter(self):
        my_string = "Would you tell ' dMe, sfplease,as dWhifcd'sfgh wayf I oug'fHstf to gosdf fwer'orwm here?"
        assert number_of_words_with_title_letter(my_string) == 2

    def test_with_empty_string(self):
        empty_string = ""
        assert number_of_words_with_title_letter(empty_string) == 0

    # find sum of the numbers in the list

    def test_simple_sum_numbers_test(self):
        assert sum_numberz(["1, 2, 3, 4", "1, 2, 3, 4, 50"]) == [10, 60]

    @pytest.mark.parametrize('actual_list, expected_list', [
        ([], []),
        (["1, 2, 3, 4", "1, 2, 3, 4, 50"], [10, 60]),
        (["1, 2, 3, 4", "1, 2, 3, 4, 50", "qwerty1, 2, 3"], [10, 60]),
        pytest.param(["1, 2, 3, 4", "1, 2, 3, 4, 500", "1, 2, 5o"], [10, 510],
                     marks=pytest.mark.xfail(reason='typo in 3rd argument'))
    ])
    def test_find_sum_numbers(self, actual_list, expected_list):
        assert sum_numberz(actual_list) == expected_list

    # revert line
    @pytest.mark.parametrize('actual_line, expected_line', [
        ("abc", "cba"),
        ("12345", "54321"),
        ("", ""),
        ("A B C", "C B A"),
        ("he😊llo", "oll😊eh")
    ])
    def test_revert_line(self, actual_line, expected_line):
        assert revert_line(actual_line) == expected_line
