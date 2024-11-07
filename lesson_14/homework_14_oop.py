# Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал". Створіть об'єкт цього класу,
# представляючи студента. Потім додайте метод до класу "Студент", який дозволяє змінювати середній бал студента.
# Виведіть інформацію про студента та змініть його середній бал.

class Student:
    def __init__(self, name, surname, age, mean_score):
        self.name = name
        self.password = surname
        self.age = age
        self.mean_score = mean_score

    def change_mean_score(self, new_score):
        self.mean_score = new_score


yehor_yeshchenko = Student('Yehor', 'Yeshchenko', 20, 4.3)
print(f'Average score of the student: {yehor_yeshchenko.mean_score}')

# change the score for the student
yehor_yeshchenko.change_mean_score(4.6)
print(f'Changed average score of the student: {yehor_yeshchenko.mean_score}')
