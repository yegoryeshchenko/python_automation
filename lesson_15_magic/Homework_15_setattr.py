# Створіть клас геометричної фігури "Ромб". Клас повинен мати наступні атрибути:
#
# сторона_а (довжина сторони a).
# кут_а (кут між сторонами a і b).
# кут_б (суміжний з кутом кут_а).
# Необхідно реалізувати наступні вимоги:
#
# Значення сторони сторона_а повинно бути більше 0.
# Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180
# Протилежні кути ромба завжди рівні, тому при заданому значенні кут_а, значення кут_б обчислюється автоматично.
# Для встановлення значень атрибутів використовуйте метод __setattr__

class Rhombus:
    def __init__(self, side, angle_a):
        self.__setattr__('side', side)
        self.__setattr__('angle_a', angle_a)

    def __setattr__(self, key, value):
        if key == 'side':
            if value <= 0:
                raise ValueError("Side should be more than 0")
            super().__setattr__(key, value)

        elif key == 'angle_a':
            if not (0 < value < 180):
                raise ValueError("Angle should be from 0 to 180 degrees")
            super().__setattr__(key, value)
            super().__setattr__('angle_b', 180 - value)

        elif key == 'angle_b':
            super().__setattr__(key, value)

    # <why {self.side} and {self.angle_b} are underlined ? tried for __str__ - the same>
    # we use __repr__ here to show the attributes along with their values in output
    def __repr__(self):
        return f'Rhomb(side = {self.side}, angle_a = {self.angle_a}, angle_b = {self.angle_b})'


# valid rhombus
try:
    rhombus1 = Rhombus(side=5, angle_a=60)
    print(rhombus1)
except ValueError as e:
    print(e)

# invalid side
try:
    rhombus2 = Rhombus(side=-5, angle_a=60)
    print(rhombus2)
except ValueError as e:
    print(e)

# invalid type side
try:
    rhombus3 = Rhombus(side='5', angle_a=60)
    print(rhombus3)
except TypeError as e:
    print(e)

# invalid angle: angle_a = 180, the other angle should not be 0
try:
    rhombus4 = Rhombus(side=20, angle_a=180)
    print(rhombus4)
except ValueError as e:
    print(e)

# invalid angle: angle_a should not be equal to 0
try:
    rhombus5 = Rhombus(side=20, angle_a=0)
    print(rhombus5)
except ValueError as e:
    print(e)
