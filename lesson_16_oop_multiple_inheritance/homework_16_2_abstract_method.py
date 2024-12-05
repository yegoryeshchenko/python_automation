# Завдання 2
# Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру.
# Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи для площі та периметру.
# Властивості по типу “довжина сторони” й т.д. повинні бути приватними, та ініціалізуватись через конструктор.
# Створіть Декілька різних об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної.

import math
from abc import abstractmethod


class Figure:

    @abstractmethod
    def square(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def __str__(self):
        return f'{self.__class__.__name__} with square {self.square():.2f} and perimeter {self.perimeter():.2f}'


class Square(Figure):

    def __init__(self, side):
        self.__side = side

    def perimeter(self):
        return self.__side * 4

    def square(self):
        return self.__side ** 2


class Rectangle(Figure):

    def __init__(self, side_1, side_2):
        self.__side_1 = side_1
        self.__side_2 = side_2

    def perimeter(self):
        return (self.__side_1 + self.__side_2) * 2

    def square(self):
        return self.__side_1 * self.__side_2


class Circle(Figure):

    def __init__(self, radius):
        self.__radius = radius

    def perimeter(self):
        return math.pi * self.__radius * 2

    def square(self):
        return math.pi * self.__radius ** 2


figures = []
figures.extend([Square(7), Square(2), Rectangle(4, 8), Rectangle(2, 1), Circle(6), Circle(1)])

for figure in figures:
    print(figure)
