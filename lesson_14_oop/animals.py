class Animal:
    base_class = 'Animal class asd'

    def make_sound(self):
        print('Animal sound')

    def go_sleep(self):
        print('I go sleep')


class Dog(Animal):
    def make_sound(self):
        print('Rrrr')


class Cat(Animal):
    def make_sound(self):
        print('Meow')


patron = Dog()
lazy_cat = Cat()
unknown = Animal()

patron.make_sound()
lazy_cat.make_sound()
unknown.make_sound()
patron.go_sleep()

lazy_cat.go_sleep()
