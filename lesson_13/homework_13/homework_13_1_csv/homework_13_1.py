# Завдання 1:
# Візміть два файли з теки ideas_for_test/work_with_csv порівняйте на наявність дублікатів і приберіть їх.
# Результат запишіть у файл result_<your_second_name>.csv

import csv

from lesson_13.homework_13.homework_13_1_csv.custom_exception import HeaderIsNotValidException

RANDOM_CSV_FILE = 'random.csv'
RANDOM_MICHAELS_CSV_FILE = 'random-michaels.csv'


# get all rows from csv except header
def get_list_of_rows_from_csv(csv_file_path):
    with open(csv_file_path, 'r', newline='') as csv_reader:
        reader = list(csv.reader(csv_reader))

        return reader[1:]


# get header from csv
def get_header_from_file(csv_file_path):
    with open(csv_file_path, 'r', newline='') as csv_reader:
        reader = list(csv.reader(csv_reader))

        return tuple(reader[0])


list_1 = get_list_of_rows_from_csv(RANDOM_CSV_FILE)
list_2 = get_list_of_rows_from_csv(RANDOM_MICHAELS_CSV_FILE)


# get common header, of they are not same, raise an exception
def get_common_header(h_1, h_2) -> str:
    # check if header is same in both files
    if h_1 == h_2:
        return h_1
    else:
        raise HeaderIsNotValidException('Header is not valid!')


# get unique rows
def get_unique_rows(lst_1, lst_2) -> set:
    common_header = get_common_header(get_header_from_file(RANDOM_CSV_FILE),
                                      get_header_from_file(RANDOM_MICHAELS_CSV_FILE))

    data1 = tuple(tuple(sublist) for sublist in lst_1)
    data2 = tuple(tuple(sublist) for sublist in lst_2)

    final_data = set(data1) | set(data2)
    final_data_list = list(final_data)
    final_data_list.insert(0, common_header)

    return final_data_list


# write to a result csv
def write_to_csv(output_csv_file, csv_data):
    with open(output_csv_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(csv_data)


result_data = get_unique_rows(list_1, list_2)
write_to_csv('output_csv_dz.csv', result_data)
