# 1. Напишіть декоратор, який логує аргументи та результати викликаної функції.
import logging


def log_args_and_result(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments: {args}")

        result = func(*args)

        print(f"Result: {result}")

        return result

    return wrapper


@log_args_and_result
def rectangle_area(side_a, side_b):
    return side_a * side_b


side_1 = 5
side_2 = 3
print("Calculate rectangle area with decorator:")
rectangle_area(side_1, side_2)

# 2. Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def exception_handling(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Function: {func.__name__} was called with the arguments: {args}, {kwargs}")
        try:

            result = func(*args, **kwargs)

            logging.info(f"Function {func.__name__} successfully executed, result is: {result}")
            return result
        except Exception as e:
            logging.error(f"The following exception occurred {func.__name__}: {e}")
            return None

    return wrapper


@exception_handling
def write_to_file(filename, text):
    with open(filename, 'w') as file:
        file.write(text)
    return f"Text was written to the {filename} file"


print("\nWrite to file WITHOUT exceptions")
write_to_file('file_to_write_text.txt',
              'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt')
print("\nWrite to file WITH exceptions")
write_to_file('/non_existing_folder/negative_case_file.txt', 'Negative test case text file content')
