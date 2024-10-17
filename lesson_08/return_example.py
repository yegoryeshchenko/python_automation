def print_first_n_records(n: int, lst: list):
    return lst[:n]


print(print_first_n_records(4, ['a', 'b', 'c', 'd', 'e', 'f', 'g']))


def print_first_n_records(n: int, lst: list):
    new_lst = []
    for k in lst[:n]:
        new_lst.append(k)

    return new_lst
