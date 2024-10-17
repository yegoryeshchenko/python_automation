
user_income = input('Ввудіть суму доходу клієнта\n')

def calculate_tax(user_income):

    # В змінній user_income ВЖЕ Є дохід користувача. Запитувати не треба.
    # Напиши свій код тут. Запиши результат в змінну tax_amount.
    if user_income < 10000:
        tax_amount = user_income * 0.1
    if user_income >=10000 and user_income < 50000:
        tax_amount = user_income * 0.15
    if user_income >= 50000:
        tax_amount = user_income * 0.20
    return tax_amount
