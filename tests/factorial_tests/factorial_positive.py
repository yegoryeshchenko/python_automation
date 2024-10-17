import unittest

# #######################
import sys
import pathlib

# sys.path  - сюди буду додавати шлях до кореня проекту
# pathlib.Path(__file__) - шлях до поточного файлу
print(f'file path: {pathlib.Path(__file__)}')
print(f'root path: {pathlib.Path(__file__).parent.parent.parent}')
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent))
print(f'sys path: {sys.path}')
# #######################

from test_functions import factorial


class FactorialPositiveTest(unittest.TestCase):  # CamelCase

    def test_factorial_5(self):  # snake_case
        actual_result = factorial(5)
        expected_result = 120

        self.assertEqual(expected_result, actual_result)

    def test_factorial_0(self):  # snake_case
        actual_result = factorial(0)
        expected_result = 1

        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
