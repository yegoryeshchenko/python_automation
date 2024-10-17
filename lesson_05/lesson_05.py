# кортеж, список, сет, dict

# my_names = ('den', 'alex', 'victor')
#
# print(my_names)
# print(my_names[0])
# print('-'*80)
#
# for name in my_names:
#     print(name)
# print('-'*80)
# print(my_names[1:])
# # -------------------
#
# my_name, alex_name, *not_my_names = ('den', 'petya','alex', 'victor')
# print(alex_name)
# print(type(not_my_names))
#
# # --------------------------------------------
# some_text = 'bla-bla'
# tuple_text = tuple(some_text)
# print(tuple_text)
#
# my_list = [1,2]
# my_tuple_with_evr = (1, my_list, 'asd', None, (1,2))
# my_list.append([1,2,3])
# my_list.append([None, True])
# print(my_tuple_with_evr)
#
# print(type(()))
# not_a_tuple = (2, )
# --------------------------------------------
# lists
my_names = ["den", "petya", "kostian"]
print(id(my_names))
print(my_names)


# --------------------------------------------
# my_names.insert(0, "vasilisa")
text_with_names = "Is we miles ready he might going. Own books built put civil fully blind fanny. Projection " \
                  "appearance at of admiration no. As he totally cousins warrant besides ashamed do. Therefore by" \
                  " applauded acuteness supported affection it. Except had sex limits county enough the figure " \
                  "former add. Do sang my he next mr soon. It merely waited do unable."

list_with_text = text_with_names.split()

list_of_names = []
for word in list_with_text:
    # print(f'check {word}: {word.istitle()}')
    if word.istitle():
        list_of_names.append(word)

print(list_of_names)

for word in list_of_names:
    list_with_text.remove(word)

print(' '.join(list_with_text))
































