class Car:
    class_name = 'Car'

    def __init__(self, brand, model, tank):
        self.brand = brand
        self.model = model
        self.tank = tank

    def go_somewhere(self, amount_in_km):
        if self.tank >= amount_in_km:
            self.tank = self.tank - amount_in_km
            print('Driving')
        else:
            print("Not enough fuel")

    def set_tank(self, value):
        self.tank = value


class Auto:
    def __init__(self, model, color, engine, fuel_to_km=0.2):
        self.model = model
        self.color = color
        self.engine = engine

        self.tank = 0

        self.__fuel_to_km = fuel_to_km

    def drive_to_nearest_town(self, distance_km):
        if self.tank / self.__fuel_to_km >= distance_km:
            self.tank = self.tank - distance_km * self.__fuel_to_km
            print("Driving..")
        else:
            print(f"can't go there, not enough fuel, fuel only on {self.tank / self.__fuel_to_km}")


class Nissan(Auto):
    brand = 'NISSAN'  # class attribute
    base_country = 'Japan'  # class method

    @classmethod
    def say_greetings(cls):
        print(f'Hello from {cls.brand}')

    def say_greetings_not_class_method(self):
        print(f'Hello from {self.brand}')


x5 = Car(brand='BMW', model='X5', tank=50)  # instance, екземпляр

print(x5.class_name)
print(x5.brand)
print(x5.model)
x5.go_somewhere(50)
x5.go_somewhere(50)

polo = Car(brand='VW', model='polo', tank=50)  # instance, екземпляр
print(polo.class_name)
print(polo.brand)
print(polo.model)

y61 = Nissan(model='y61', color='green', engine='3.0', fuel_to_km=0.1)  # fuel_to_km - value by default
y61_1 = Nissan(model='y61', color='green', engine='3.0')
navara = Nissan(model='y61', color='black', engine='5.2')

y61.tank = 70

y61.drive_to_nearest_town(400)
y61.drive_to_nearest_town(400)

print(y61.color)
y61.color = 'Red'
print(y61.color)


Nissan.say_greetings() # class method
y61_1.say_greetings_not_class_method() # without class method
Nissan.say_greetings_not_class_method(navara)  #