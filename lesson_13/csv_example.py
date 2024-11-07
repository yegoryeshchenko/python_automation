import csv

# Дані для запису у CSV-файл
data = [
    ['Name', 'Age', '', 'Bool'],
    ['John', 30, 'New York', False],
    ['Alice', 25, 'Los Angeles', None],
    ['Bob', None, 'Chicago', True]
]


# Відкриття CSV-файлу для запису
with open('output.csv', 'w', newline='') as csvfile:

    writer = csv.writer(csvfile)
    writer.writerows(data)


with open('output.csv', 'r') as some_variable_csv:

    reader = list(csv.reader(some_variable_csv))

    header = reader[0]
    row_data = reader[1:]

    print('Header is:', header)
    for index, row in enumerate(row_data, start=1):  # enumerate index, row
        print(f'{index} row is :', row)
