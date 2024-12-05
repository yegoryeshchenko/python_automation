class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __del__(self):
        print(f"The {self.make} {self.model} object was destroyed")


a = 5
my_car = Car('1', '2')

del my_car
print(type(a))
del a
