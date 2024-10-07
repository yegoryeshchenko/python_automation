# Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h"
# (враховуються як великі так і маленькі). Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".

def input_word():
    entered_word = input("Введіть слово яке містить літеру 'h' у верхньому або нижньому регістрі:\n")
    print(f"Ви ввели слово '{entered_word}'")
    return entered_word


print("Solution 1 - with counter")
counter = 0
while True:
    word = input_word()
    for char in word:
        if char == 'h' or char == 'H':
            counter += 1
            if counter > 0:
                break
    if counter > 0:
        print("Слово містить літеру 'h' або 'H'. Програма завершена.")
        break
    else:
        print("Слово не містить літери 'h'. Будь ласка, повторіть спробу")


print("\n\nSolution 2 - with flag, shorter")
while True:
    word = input_word()
    contains_symbol = False
    for char in word:
        if char == 'h' or char == 'H':
            contains_symbol = True
            break
    if contains_symbol:
        print("Слово містить літеру 'h' або 'H'. Програма завершена.")
        break
    else:
        print("Слово не містить літери 'h'. Будь ласка, повторіть спробу.")
