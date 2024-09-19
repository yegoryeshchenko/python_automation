# task 01 == Виправте синтаксичні помилки
print("Hello", "world", "!", sep=" ")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"

if True:
    print(f"{hello}  {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = 4 * apples

# task 05 == виправте назви змінних
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimetery = storona_1 + storona_2 + storona_3 + storona_4
print(perimetery)


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
apple_trees = 4
pear_trees = apple_trees + 5
plum_trees = apple_trees - 2

total_trees_in_the_garden = apple_trees + pear_trees + plum_trees

print(f"Відповідь: всього в саду посадили {total_trees_in_the_garden} дерев")

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
temp_before_lunch = 5
temp_after_lunch = temp_before_lunch - 10
temp_evening = temp_after_lunch + 4
print(f"Відповідь: надвечір температура становила {temp_evening} градус(ів)")

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
boys = 24
girls = boys / 2
absent_children = 1 + 2
total_number_of_children_today = boys + girls - absent_children
print(f"Відповідь: у театральному гуртку сьогодні {total_number_of_children_today} дітей")

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
book_1 = 8
book_2 = book_1 + 2
book_3 = (book_1 + book_2) / 2
total_amount_for_three_books = book_1 + book_2 + book_3

print(f"Відповідь: всі 3 книги коштуватимуть {total_amount_for_three_books} гривень")