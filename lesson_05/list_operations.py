print(['a', 'b', 'c', 'c'].index('c'))

my_names = ['den', 'alex', 'ivan', 'divan', 'long wrd', 'r']
my_ages = [1, 2, 3, 5, 2, 3]

# sorted_names = sorted(my_names, reverse=True)
# sorted_ages = sorted(my_ages)

# print(sorted_names)
# print(sorted_ages)


my_names.sort(reverse=True)
print(my_names)

sorted_names_by_default = sorted(my_names)


def my_fn(word):
    return len(word)


sorted_names_by_len = sorted(my_names, key=my_fn, reverse=True)
print(sorted_names_by_len)

my_list_1 = [1, 2, 3, ' Alex', [1, 0], None]

# my_list_2 = list('Alex', 'Den')
# print(my_list_2)

my_tuple = (1, 2, 3, 4)
my_list_3 = list(my_tuple)

my_numbers = [1, 2, 3, 4]

sq_list = []
for num in my_numbers:
    sq_list.append(num ** 2)

print(sq_list)

sq_list_lc = [num ** 2 for num in my_numbers if num % 2 == 0]
print(sq_list_lc)

my_range_list = range(40, 20, -2)
print(list(my_range_list))

sq_list_100 = [k ** 2 for k in range(1, 101)]
print(sq_list_100)
