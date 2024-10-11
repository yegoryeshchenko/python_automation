# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""

print("task 1")


def multiplication_table(number):
    if number <= 0:
        print("Please enter the number more than zero")
        return
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помилка, а може не одна
        if result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1


print(f"result of multiplication_table(number) program:")
multiplication_table(3)
multiplication_table(0)
multiplication_table(-1)

# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
#  Написати функцію, яка обчислює суму двох чисел.
print("\ntask 2")


def summarize(term_1, term_2):
    return term_1 + term_2


print("result of the function that summarizes 2 numbers:")
print(summarize(3, 4))

# task 3
#  Написати функцію, яка розрахує середнє арифметичне списку чисел.
print("\ntask 3")


def mean(list_of_numbers):
    try:
        if not all(isinstance(num, (int, float)) for num in list_of_numbers):
            raise ValueError("The list contains incorrect values, please enter int or float values")
        mean_value = sum(list_of_numbers) / len(list_of_numbers)
        return mean_value

    except ZeroDivisionError:
        return "List is empty"

    except ValueError as value_error:
        return str(value_error)


print("Calculation of the mean value:")
print(mean([1, 2, 3, 4.04, 5]))
print(mean([12]))
print(mean([1, 'some_text', 3, 4, 5]))
print(mean([]))

# task 4
#  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
print("\ntask 4")


def revert_line(line):
    return line[::-1]


print("Revert the line:")
print(revert_line("a b c d e f g h"))

# task 5
#  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
print("\ntask 5")


def find_the_longest_word(list_of_words):
    if not list_of_words:
        return None
    return max(list_of_words, key=len)


initial_list = ["abc", "abcd", "abcde", "absdefg", "a", "45"]
print(f"Find the longest word by criteria - key=len. \nInitial list: {initial_list}")
print(find_the_longest_word(initial_list))

# task 6
print("\ntask 6")
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""


def find_substring(str_1, str_2):
    return str_1.find(str_2)


str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))  # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))  # поверне -1

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
# task 7
print("task 7")
print("task 06 homework 1 (perimetery)")


# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
def calculate_perimeter(side_1, side_2, side_3, side_4):
    """
    function to calculate perimeter of a quadrangle by its sides' lengths
    :param side_1: length of one side 1 of a quadrangle
    :param side_2: length of one side 2 of a quadrangle
    :param side_3: length of one side 3 of a quadrangle
    :param side_4: length of one side 4 of a quadrangle
    :return: perimeter of a quadrangle
    """
    try:
        sides = [side_1, side_2, side_3, side_4]
        if not all(side > 0 for side in sides):
            raise ValueError("Усі сторони повинні бути додатними значеннями більше нуля.")

        perimeter = side_1 + side_2 + side_3 + side_4
        return perimeter

    except ValueError as value_error:
        return str(value_error)


side_1 = 5
side_2 = 10
side_3 = 5
side_4 = 10
print(f"\nPerimeter calculation:\n perimeter({side_1}+{side_2}+{side_3}+{side_4}) ="
      f" {calculate_perimeter(side_1, side_2, side_3, side_4)}")

# task 8
print("\ntask 8")
print("task 3_02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті")


def find_all_occurrences_of_a_symbol(string_to_analyze, char_to_find):
    """
    finds all the occurrences of a given symbol 'char_to_find' in a given string 'my_string'
    :param string_to_analyze: string (text) to analyze
    :param char_to_find: char to find in the given text
    :return: list of occurrences of a given char_to_find
    """
    return [char for char in string_to_analyze if char == char_to_find]


my_char = "'"
my_string = "Would you tell ' dMe, sfplease,as dWhifcd'sfgh wayf I oug'fHstf to gosdf fwer'orwm here?"
print(f"Occurrences of symbol {my_char} in the given string: "
      f"{find_all_occurrences_of_a_symbol(my_string, my_char)}")

# task 9
print("\n task 9")
print("task 4_05 Виведіть, скільки слів у тексті починається з Великої літери?")


def number_of_words_with_title_letter(some_text):
    """
    returns number of the words in text 'some_text', that start from a capital letter
    :param some_text: text to analyze
    :return: title_count: int - number of words that start from capital letter
    """
    title_count = 0
    for word in some_text.split():
        if word.istitle():
            title_count += 1
    print(f"{title_count} слів у тексті починається з великої літери")
    return title_count


number_of_words_with_title_letter("Would you tell Me, please, Which way I ougHt to go from here?")

# task 10
print("\ntask 10")
print("Homework 5_1")


def filter_cars_by_criteria(cars_catalog: dict, criteria: tuple) -> list[tuple]:
    """
    function filters cars by search criteria (year_min>=year, engine_volume>=volume, price<=price_value)
    returns first 5 filtered results
    :param criteria: tuple
    :param cars_catalog:
    :return: sorted_cars: list[tuple] - list of first 5 filtered results
    """
    # search criteria
    year_min, engine_min, price_max = criteria
    # filter the cars by search criteria
    filtered_cars = [
        (name, details) for name, details in cars_catalog.items()
        if details[1] >= year_min and details[2] >= engine_min and details[4] <= price_max
    ]

    # sort cars by price ascending:
    sorted_cars = sorted(filtered_cars, key=lambda x: x[1][4])

    # print first 5 search results
    print("The following car corresponds the search criteria:")
    for name, details in sorted_cars[:5]:
        print(f"{name}, color: {details[0]}, year: {details[1]}, engine volume: {details[4]}")
    return sorted_cars[:5]


car_data = {
    'Mercedes': ('silver', 2019, 1.8, 'sedan', 50000),
    'Audi': ('black', 2020, 2.0, 'sedan', 55000),
    'BMW': ('white', 2018, 3.0, 'suv', 70000),
    'Lexus': ('gray', 2016, 2.5, 'coupe', 45000),
    'Toyota': ('blue', 2021, 1.6, 'hatchback', 25000),
    'Honda': ('red', 2017, 1.5, 'sedan', 30000),
    'Ford': ('green', 2019, 2.3, 'suv', 40000),
    'Chevrolet': ('purple', 2020, 1.4, 'hatchback', 22000),
    'Chrysler': ('gray', 2016, 2.4, 'sedan', 22000),
    'Dodge': ('yellow', 2020, 3.6, 'suv', 40000),
    'Ferrari': ('red', 2019, 4.0, 'coupe', 500000),
    'Lamborghini': ('orange', 2021, 5.0, 'coupe', 800000),
    'Maserati': ('blue', 2018, 4.7, 'coupe', 100000),
    'Bugatti': ('black', 2020, 8.0, 'coupe', 2000000),
    'McLaren': ('yellow', 2017, 4.0, 'coupe', 700000),
    'Rolls-Royce': ('white', 2019, 6.8, 'sedan', 500000),
}

search_criteria = (2010, 1.6, 40000)
filter_cars_by_criteria(car_data, search_criteria)
