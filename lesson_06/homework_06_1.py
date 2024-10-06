# Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()

words = input('Please input text to analyze:\n')

print(list(words))


def is_number_of_unique_chars_more_than_10(number_of_unique_symbols: int):
    print(f"Кількість унікальних символів складає {number_of_unique_symbols}")
    if number_of_unique_symbols > 10:
        print(True)
    else:
        print(False)


print("\nSolution 1: for - loop")
unique_chars = []
for char in words:
    if char not in unique_chars:
        unique_chars.append(char)
number_of_chars = len(unique_chars)
number_of_unique_chars_solution_1 = int(number_of_chars)
is_number_of_unique_chars_more_than_10(number_of_unique_chars_solution_1)

print("\nSolution 2:")
number_of_unique_chars_solution_2 = len(''.join(set(words)))
is_number_of_unique_chars_more_than_10(int(number_of_unique_chars_solution_2))

print("\nSolution 3 (too simple to be correct, but it works :))")
number_of_unique_chars_solution_3 = len(set(words))
is_number_of_unique_chars_more_than_10(int(number_of_unique_chars_solution_3))
