class Car:
    def __init__(self, make, model):
        self.make = make  # Public attribute
        self._model = model  # Protected attribute
        self.__year = 2022  # Private attribute

    def display_model(self):
        print(f"Model: {self._model}")

    def update_year(self, new_year):
        self.__year = new_year


# Створення об'єкта та використання атрибутів та методів
my_car = Car("Toyota", "Camry")
print(my_car.make)  # Public attribute, виведе: Toyota
my_car.display_model()  # Protected method, виведе: Model: Camry
# my_car.update_year(2023)  # Private attribute update

print(my_car.make)
