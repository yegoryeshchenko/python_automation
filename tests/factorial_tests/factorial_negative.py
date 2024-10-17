import unittest

# #######################
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent))
# #######################

from test_functions import factorial


class FactorialNegativeTest(unittest.TestCase):  # CamelCase

    def test_factorial_put_minus_1_negative(self):
        number = -1
        expected_msg = f'You have to use 0 or positive numbers. You put {number}'

        with self.assertRaises(ValueError) as type_error:
            factorial(number)

        exception = type_error.exception
        actual_error_msg = exception.args[0]

        self.assertEqual(expected_msg, actual_error_msg, msg='some custom text')

    def test_factorial_put_string_negative(self):
        with self.assertRaises(TypeError):
            factorial('asd')


if __name__ == '__main__':
    unittest.main(verbosity=2)
