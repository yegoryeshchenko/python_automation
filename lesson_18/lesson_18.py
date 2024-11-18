list_of_numbers1 = [11, 12, 13, 14, 15]
list_of_numbers2 = [21, 22, 23, 24, 25]

# iter()
# next()

iter_obj = iter(list_of_numbers1)
iter_obj2 = iter(list_of_numbers2)

# print(next(iter_obj))  # 0
# print(next(iter_obj))  # 1
# print(next(iter_obj2))  # 0
# print(next(iter_obj2))  # 1
# print(next(iter_obj))  # 2
# print(next(iter_obj2))  # 3
# print(next(iter_obj))  # 3
# print(next(iter_obj))  # 4

try:
    while True:
        print(next(iter_obj))
except StopIteration:
    pass
