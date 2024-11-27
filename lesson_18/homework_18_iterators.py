# 1. Реалізуйте ітератор для зворотного виведення елементів списку.
class ReverseIterator:
    def __init__(self, lst):
        self.lst = lst
        self.index = len(lst) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        value = self.lst[self.index]
        self.index -= 1
        return value


my_list = [1, 2, 3, 4, 'asd', '&^%']
reverse_iterator = ReverseIterator(my_list)

print("Reverse list with iterator:")
for item in reverse_iterator:
    print(item)


# 2. Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.
class EvenNumbersIterator:

    def __init__(self, n_number):
        self.n = n_number
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        value = self.current
        self.current += 2
        return value


print("\nReturn even numbers with iterator")
n = 15
even_iterator = EvenNumbersIterator(n)

for num in even_iterator:
    print(num)
