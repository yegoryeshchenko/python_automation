# Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який сформує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1.
# Данні в лісті можуть бути будь якими

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']

print('Solution 1 - check by type')
lst2 = []
for item in lst1:
    if type(item) is str:
        lst2.append(item)
print(lst2)


print("\nSolution 2 - using isinstance()")
lst2 = [item for item in lst1 if isinstance(item, str)]
print(lst2)
