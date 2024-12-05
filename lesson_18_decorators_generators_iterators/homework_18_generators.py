# 1. Напишіть генератор, який повертає послідовність парних чисел від 0 до N.

def even_numbers(n_number):
    for num in range(n_number + 1):
        if num % 2 == 0:
            yield num


print("Even numbers sequence:")
n = 10
for number in even_numbers(n):
    print(number)


# 2. Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.
def fibonacci_sequence(n_number):
    a, b = 0, 1
    while a <= n_number:
        yield a
        a, b = b, a + b


print("\nFibonacci sequence:")
n = 20
for fib in fibonacci_sequence(n):
    print(fib)
