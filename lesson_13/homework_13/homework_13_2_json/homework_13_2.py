# Завдання 2:
# Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json є валідними json.
# результат для невалідного файлу виведіть через логер на рівні еррор у файл json__<your_second_name>.log


import os
import json
import logging

logging.basicConfig(
    filename='json__yeshchenko.log1',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def validate_jsons(directory_to_check):
    for filename in os.listdir(directory_to_check):
        file_path = os.path.join(directory_to_check, filename)

        if os.path.isfile(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    json.load(f)
            except json.JSONDecodeError as e:
                logging.error(f"File '{filename}' is not a valid JSON: {e}")


validate_jsons('work_with_json')
