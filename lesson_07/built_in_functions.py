# all()
# print(all([True, False, True]))
# print(all([True, True]))
#
#
def is_even(number):
    return number % 2 == 0


#
#
# print(is_even(5))
# print(is_even(10))
#
# result = [is_even(num) for num in [2, 4, 6, 7]]
# print(result)
# print([is_even(num) for num in [2, 4, 6, 7]])
#
# print(all(result))


for k in enumerate(['den', 'alex'], start=15):
    print(k)

for ind, name in enumerate(['den', 'alex'], start=0):
    print(f"name {name} has index {ind}")

print([num for num in range(20) if is_even(num)])

print(list(filter(is_even, range(20))))

my_descr = "My name is Den".split(' ')
print([k for k in my_descr if len(k)])

res = []
for k in my_descr:
    if len(k):
        res.append(k)
print(res)

print(list(filter(len, my_descr)))

print(list(map(len, my_descr)))
print(list(len(k) for k in my_descr))

print(pow(5, 5))


len_of_elements = list(map(len, my_descr))

print(list(zip(range(100), my_descr, len_of_elements)))





