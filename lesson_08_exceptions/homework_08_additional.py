# доп задача:
# Напишіть інтерактивний калькулятор. Передбачається, що користувач вводить формулу, що складається з числа, оператора
# (як мінімум * і /) та іншого числа, розділених пробілом (наприклад, 2 * 5).
# Якщо вхідні дані не складаються з трьох елементів, генеруйте та спіймайте власний ексепшн FormulaError.
# Якщо другий елемент не є «*» або «/», генеруйте та спіймайте власний ексепшн WrongOperatorError
# Якщо введені числа не int або float спіймайте ValueError
# Також ловіть помилку при діленні на 0
# В кожній спійманій помилці друкуйте пояснення, що пішло не так
# Надайте три спроби скористуватись калькулятором, якщо введені не вірні дані, якщо не вийшло - прінтайте що закінчились спроби
# Результат виконання формули - float число з двома знаками після крапки

class FormulaError(Exception):
    def __init__(self, formula):
        self.formula = formula
        message = f'\"{formula}\" should consist of 3 elements!'
        super().__init__(message)


class WrongOperatorError(Exception):
    def __init__(self, operator):
        self.operator = operator
        message = f'\"{operator}\" operator is invalid!'
        super().__init__(message)


def calculate(operator, num_1, num_2):
    try:
        if operator == '*':
            result = num_1 * num_2
            return result
        elif operator == '/':
            result = num_1 / num_2
            return result
        else:
            raise WrongOperatorError(operator)
    except ZeroDivisionError as zde:
        print(zde)
        return None


def calculator():
    attempts = 3
    while attempts > 0:
        formula = input('Please enter the formula in format (a <operator> b), where operator is "*" or "/": ')
        try:
            parts = formula.split(' ')
            if len(parts) != 3:
                raise FormulaError(formula)

            num_1, operator, num_2 = parts

            try:
                num_1 = float(num_1)
                num_2 = float(num_2)
            except ValueError:
                raise ValueError("The numbers must be int or float!")

            result = calculate(operator, num_1, num_2)
            if result is not None:
                print(f"Calculation result is: {result}")
                break

        except FormulaError as formula_error:
            print(formula_error)
        except WrongOperatorError as wrong_operator_error:
            print(wrong_operator_error)
        except ValueError as value_error:
            print(value_error)

        attempts -= 1
        if attempts == 0:
            print("You have used all your attempts.")
        else:
            print(f"Try again. You have {attempts} attempts")


calculator()
