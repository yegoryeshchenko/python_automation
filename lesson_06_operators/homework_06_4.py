# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

list_of_numbers = [1, 2, 3, 4, 5, 11, 20, 101, 50, 75, 82, 14, 13]
print(f"Initial list: '{list_of_numbers}'")

list_of_even_numbers = []
for element in list_of_numbers:
    if element % 2 == 0:
        list_of_even_numbers.append(element)

print(f"List with even numbers from the initial one: '{list_of_even_numbers}'")
print(f"Sum of elements of this list is {sum(list_of_even_numbers)}")
