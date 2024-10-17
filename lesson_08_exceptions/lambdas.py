def get_5():
    print(str(5))
    return 5


new_fn = get_5()

my_num = 5

print(id(get_5()))
print(id(new_fn))

lst_of_strings = ['ttttttasd', 'hjdttfhs', 'asadsjdfattthsf', 'tt']


def get_word_with_max_include_letter(letter):
    word = ''
    max_t = 0
    for k in lst_of_strings:
        if k.count(letter) > max_t:
            word = k
            max_t = k.count(letter)

    print(word)
    return word


get_word_with_max_include_letter('t')


def count_t(word: str):
    return word.count('t')


print(max(lst_of_strings, key=count_t))
print(max(lst_of_strings, key=lambda x: x.count('t')))

users = {
    "den": "qa",
    "alex": "not qa"
}

print(max(users.items(), key=lambda x, y: 1 if y == "qa" else 0))



