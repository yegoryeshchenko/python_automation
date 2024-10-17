import unittest


def sum_2_numbers(a, b):
    return a + b


class MyTest(unittest.TestCase):

    def test_sum_1_2(self):

        actual_result = sum_2_numbers(1,2)
        expected_result = 3

        self.assertEqual(actual_result, expected_result)  # assert actual_result == expected_result

    def test_sum_3_4(self):

        actual_result = sum_2_numbers(3,4)
        expected_result = 7

        assert actual_result == expected_result, f'expected {expected_result} == {actual_result}'

    def test_compare_2_lists_with_dicts(self):

        expected_list = [
            {
                'Name': 'Den',
                'Age': 25,
                'Position': 'QA'
            },
            {
                'Name': 'Den',
                'Age': 25,
                'Position': 'QA1'
            },
            {
                'Name': 'Den',
                'Age': 26,
                'Position': 'QA'
            },
        ]

        actual_list = [
            {
                'Name': 'Ivan',
                'Age': 25,
                'Position': 'QA'
            },
            {
                'Name': 'Den',
                'Age': 25,
                'Position': 'AQA'
            },
            {
                'Name': 'Den',
                'Age': 30,
                'Position': 'QA'
            },
        ]

        self.assertNotEqual(actual_list, expected_list)

    def test_almost_equal(self):


        self.assertAlmostEqual(5, 7, delta=3) #  7 between 5-3 and 5+3




if __name__ == '__main__':
    unittest.main()