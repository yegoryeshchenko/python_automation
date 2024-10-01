import re

adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
print("""task 01 Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")""")
task_01 = adwentures_of_tom_sawer.replace("\n", " ")
print(task_01)

# task 02 ==
""" Замініть .... на пробіл
"""
print("\ntask 02 Замініть .... на пробіл")
task_02 = adwentures_of_tom_sawer.replace("....", " ")
print(task_02)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
print("\ntask 03 Зробіть так, щоб у тексті було не більше одного пробілу між словами.")
not_more_than_one_space = ' '.join(adwentures_of_tom_sawer.split())
print(f"В реченні не більше одного пробілу: {not_more_than_one_space}")

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print('\ntask 04 Виведіть, скількі разів у тексті зустрічається літера "h"')
h_count = adwentures_of_tom_sawer.count("h")
print(f'Літера "h" зустрічається {h_count} разів')

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
print("\ntask 05 Виведіть, скільки слів у тексті починається з Великої літери?")

title_count = 0
for word in adwentures_of_tom_sawer:
    if word.istitle():
        title_count += 1
print(f"{title_count} слів у тексті починається з великої літери")

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
print("\ntask 06 Виведіть позицію, на якій слово Tom зустрічається вдруге")
tom = "Tom"
print("Solution 1:")
print(f"Знайдемо перше входження слова {tom} і індекс його останньої букви")
first_tom = adwentures_of_tom_sawer.find(tom) + len(tom)
second_tom = adwentures_of_tom_sawer.find(tom, first_tom)  # або почати з позиції first_tom + 1
if second_tom != -1:
    print(f"Знайдено на позиції {second_tom}.")
else:
    f"Слово {tom} не знайдено"

print("Solution 2")
first_tom_v2 = adwentures_of_tom_sawer.find("Tom")
# Друге входження слова "Tom"
second_tom_v2 = adwentures_of_tom_sawer.find("Tom", first_tom_v2 + 1)
if second_tom_v2 != -1:
    print(f"Знайдено на позиції {second_tom_v2}.")
else:
    f"Слово {tom} не знайдено\n"

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
print("task 07 Розділіть змінну adwentures_of_tom_sawer по кінцю речення. "
      "Збережіть результат у змінній adwentures_of_tom_sawer_sentences")
print("Solution 1 - користуючись методами string:")
adwentures_of_tom_sawer_cleaned_up = adwentures_of_tom_sawer.replace("....",
                                                                     "")  # "очищуємо" текст від зайвих символів"
# залишаємо тільки 1 пробіл як знак розділу між словами і реченнями.
adwentures_of_tom_sawer_cleaned_up = ' '.join(adwentures_of_tom_sawer_cleaned_up.split())

adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer_cleaned_up.split(". ")
print(f"Текст, розділений на речення за допомогою методів string: {adwentures_of_tom_sawer_sentences}\n")

print("Solution 2 - regular expressions:")
adwentures_of_tom_sawer_sentences_v2 = re.split(r'(?<=[.!?])\s+', adwentures_of_tom_sawer)
print(f"Текст, розділений на речення за допомогою regexp: {adwentures_of_tom_sawer_sentences_v2}\n")

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print("task 08 - Виведіть четверте речення з adwentures_of_tom_sawer_sentences. Перетворіть рядок у нижній регістр.")
print(f"Четверте речення: {adwentures_of_tom_sawer_sentences[4]}")
fourth_sentence_lower_case = adwentures_of_tom_sawer_sentences[4].lower()
print(f"Четверте речення в нижньому регістрі: {fourth_sentence_lower_case}\n")

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
print("task 09 - Перевірте чи починається якесь речення з 'By the time'")
count = 0
index = 1
for word in adwentures_of_tom_sawer_sentences:
    if word.startswith("By the time"):
        count += 1
        print(f"Sentence number {index} starts from words 'By the time'")
if count > 0:
    print(f"There are {count} sentences, that starts from 'By the time'")
    index += 1

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
print("\ntask 10 - Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.")
last_sentence = adwentures_of_tom_sawer_sentences[-1]  # - останнє речення
print("Кількість слів в останньому реченні: ")
print(len(last_sentence.split()))
