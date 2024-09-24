import math
import re

alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal ' \
                      'on where you want to get to," said the Cat.\n"I don\'t much care where ——" said Alice.\n' \
                      '"Then it doesn\'t matter which way you go," said the Cat.\n"—— so long as I get somewhere,' \
                      '" Alice added as an explanation.\n"Oh, you\'re sure to do that," said the Cat, ' \
                      '"if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
alice_in_wonderland_few_lines = '"Would you tell me, please, which way I ought to go from here?"' \
                                '"That depends a good deal on where you want to get to," said the Cat."I don\'t much \n' \
                                'care where ——" said Alice. "Then it doesn\'t matter which way you go," said the Cat.' \
                                '"—— so long as I get somewhere, " Alice added as an explanation."Oh, you\'re sure \n' \
                                'to do that," said the Cat, "if you only walk long enough."'
print(f"task 1 - Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії \n"
      f"{alice_in_wonderland_few_lines}\n")

# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
print("task 2 - Знайдіть та відобразіть всі символи одинарної лапки (') у тексті")
solution_1 = [char for char in alice_in_wonderland if char == "'"]
solution_2 = re.findall("'", alice_in_wonderland)
print(f"Solution 1: {solution_1}")
print(f"Solution 2: {solution_2}\n")

# task 03 == Виведіть змінну alice_in_wonderland на друк
print(f"task 3 - Виведіть змінну alice_in_wonderland на друк \n{alice_in_wonderland}\n")

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
print("task 4")
black_sea_square = 436402
azov_sea_square = 37800
total_square = black_sea_square + azov_sea_square
print(f"Відповідь: Чорне і Азовське моря разом займають площу {total_square} км2.\n")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""

total_products_in_three_warehouses = 375291
first_plus_second_warehouse = 250449
second_plus_third_warehouse = 222950
print("task 5")
print("Рішення")
print("Знайдемо кількість товарів на третьому складі:")
third_warehouse = total_products_in_three_warehouses - first_plus_second_warehouse
print(f"Кількість товарів на третьому складі: {third_warehouse}")
print("Знайдемо кількість товарів на другому складі:")
second_warehouse = second_plus_third_warehouse - third_warehouse
print(f"Кількість товарів на другому складі: {second_warehouse}")
print("Знайдемо кількість товарів на першому складі:")
first_warehouse = first_plus_second_warehouse - second_warehouse
print(f"Кількість товарів на першому складі: {first_warehouse}")
if first_warehouse + second_warehouse + third_warehouse == total_products_in_three_warehouses:
    print(f"Перевірка показала, що загальна сума товарів дорівнює {total_products_in_three_warehouses}.")
else:
    print("Відповідь невірна")
print(f"На першому складі {first_warehouse} товарів,\n"
      f"на другому - {second_warehouse}\n"
      f"на третьому - {third_warehouse}.\n")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
print("task 6")
amount_of_months = 18
monthly_payment_amount = 1179
total_cost = 1179 * 18
print(f"Відповідь: вартість комп’ютера становить {total_cost} гривень\n")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
print("task 7")
print(f"a) {8019 % 8}     d) {7248 % 6}\n"
      f"b) {9907 % 9}     e) {7128 % 5}\n"
      f"c) {2789 % 5}     f) {19224 % 9}\n")

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
print("task 8")
pizza_big = 274
pizza_medium = 218
juice = 35
cake = 350
water = 21
total_order_amount = pizza_big * 4 + pizza_medium * 2 + juice * 4 + cake + water * 3
print(f"Відповідь: для замовлення Іринці знадобиться {total_order_amount} гривень\n")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
print("task 9")
total_photos_amount = 232
max_photos_per_page = 8
# приводимо до int, тому що кількість має бути цілим числом
print("Solution 1")
pages_needed_solution_1 = int(total_photos_amount / max_photos_per_page)
print(f": Відповідь: Ігорю знадобиться {pages_needed_solution_1} сторінок")
print("Solution 2")
pages_needed_solution_2 = total_photos_amount / max_photos_per_page
# math.ceil() - округлення в більшу сторону, якщо "total_photos_amount / max_photos_per_page" поверне дробове число
print(f"Відповідь: Ігорю знадобиться {math.ceil(pages_needed_solution_2)} сторінок.\n")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
total_distance = 1600
tank_volume = 48
gas_consumption = 9 / 100

total_consumption = 1600 * gas_consumption
number_of_fuelings = int(total_consumption / tank_volume)
print("task 10")
print(f"Відповідь: \n"
      f"1) для такої подорожі знадобиться {total_consumption} літрів бензину\n"
      f"2) родині щонайменше потрібно заїхати {number_of_fuelings} разів на заправку.")
