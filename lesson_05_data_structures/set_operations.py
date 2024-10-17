# set - це множина хешованих (незмінних унікальних значень)

my_set = {1, 2, 3}
print(my_set)

# incorrect_set = {1, 2, 3, 4, 5, 5, [1, 2]}
# print(incorrect_set)


my_set_2 = {3, 4, 5, 7}
my_set.update(my_set_2)

print(my_set)


print(my_set.difference(my_set_2))
print(my_set.symmetric_difference(my_set_2))

print(my_set.issubset(my_set_2))