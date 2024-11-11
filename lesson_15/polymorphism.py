class Dog:
    def make_sound(self):
        return "Woof!"


class Cat:
    def make_sound(self):
        return "Meow!"


# Використання поліморфізму
animals = [Dog(), Cat()]

for animal in animals:
    print(animal.make_sound())


# Виведе:
# Woof!
# Meow!


class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meow!"


# Використання поліморфізму
animals = [Dog("Buddy"), Cat("Whiskers")]

for animal in animals:
    print(f"{animal.name} says: {animal.make_sound()}")
# Виведе:
# Buddy says: Woof!
# Whiskers says: Meow!
