my_name = 'Yehor'

# print(my_name[2])
# # slices
# print(my_name[:4])
# print(my_name[1:])
# print(my_name[1:4])
# print(my_name[::2])
# print(my_name[1::2])

print(my_name)
print(id(my_name))
my_five_name = my_name * 5
print(my_name)
print(id(my_name))

his_name = 'Yehor'
print(id(my_name))
print(id(his_name))

print('=============================================')

sent = "Lorem     Ipsum  is simply dummy, text of the sprinting and tyypesetting, industry. Lorem Ipsum has been the industry's"

# my_phrases = sent.split(",")

print(sent.split(",")[0])
print(sent.split(",")[1])
print(sent.split(",")[2])

first_case = sent.split()
# print(first_case)
second_case = sent.split(' ')
# print(second_case)

index = 0
for word in first_case:
    new_element = f"index is {index} is element: {word}"
    # print(new_element)
    index += 1

print(sent.startswith('Lorem'))
for word in sent.split():
    print(f'is {word} starts with s: {word.startswith("s")}')

print(sent.replace('Lorem', 'Merol'))

# joins
sent = "Would you tell me, please, which way I ought to go from here? That depends a good deal "
list_of_words = sent.split()

print(type(list_of_words))
print(list_of_words)
# join
join_string = ' | '.join(list_of_words)
print(type(join_string))
print(join_string)

initial_str = "2023-04-27 15:30:45 - TestCase: login_successful"
test_case = "TestCase: "
# index = initial_str.index(test_case) + len(test_case)-1
# print(index)
# replaced = initial_str[index:]
# print(replaced)

test_string = ""
parts = initial_str.split('TestCase: ')
if len(parts) > 1:
    test_string = parts[1].strip()


def check_file_format(file_list: list, extention: str):
    new_list = []
    # YOUR CODE HERE
    for file in file_list:
        if file.endswith(extention):
            new_list.append(file)
    return new_list

# first_tom_v2 = adwentures_of_tom_sawer.find("Tom")
# # Друге входження слова "Tom"
# second_tom_v2 = adwentures_of_tom_sa
# wer.find("Tom", first_tom_v2 + 1)
# if second_tom_v2 != -1:
#     print(f"Знайдено на позиції {second_tom_v2}.")
# else:
#     f"Слово {tom} не знайдено\n"
filetext = "mndbfmnsdf"
filetext.replace("", "")

# def change_params(old_value:str, new_value:str):
filetext = """\
screen_size = 800x600
paralel_processes = 10
db_conection = localhost:5432"""
# YOUR CODE HERE
index = filetext.find("=")

print(index)
