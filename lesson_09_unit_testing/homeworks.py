# Створіть нову гілку, яка буде використовуватись для змін, за допомогою команди git checkout -b homework08.
# Можна також використовувати формат: назва_дз_номер_лекції.
# Cтворіть папку lesson_08 у репозиторії
# Оберіть від 3 до 5 різних домашніх завдань
# перетворюєте їх у функції (якщо це потрібно)
# створіть в папці файл homeworks.py куди вставте ваші функції з дз
# та покрийте їх не менш ніж 10 тестами (це загальна к-сть на все ДЗ).
# імпорт та самі тести помістіть в окремому файлі - test_homeworks08.py
# На оцінку впливає як якість тестів так і розмір тестового покриття. Мінімум на 10 балів - 1 правильно задизайнений
# позитивний тест на функцію.

# або на test_functions.py

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


def find_all_occurrences_of_a_symbol(string_to_analyze, char_to_find):
    """
    finds all the occurrences of a given symbol 'char_to_find' in a given string 'my_string'
    :param string_to_analyze: string (text) to analyze
    :param char_to_find: char to find in the given text
    :return: list of occurrences of a given char_to_find
    """
    return [char for char in string_to_analyze if char == char_to_find]


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


def sum_numberz(list_for_sum: list):
    results = []
    for item in list_for_sum:
        try:
            numbers = item.split(',')

            sum_per_item = sum(int(num) for num in numbers)
            results.append(sum_per_item)
            print(sum_per_item)

        except ValueError:
            print(f"Не можу це зробити")
    return results


def revert_line(line):
    return line[::-1]