
import pathlib
import os

current_dir = pathlib.Path().absolute()

print(type(current_dir))
print(current_dir.name)
print(current_dir.parent)

parents = current_dir.parents

for par in parents:
    print(par)

for path_ in current_dir.iterdir():
    if path_.is_file():
        print(path_.name)

print('-' * 80)

for path_ in current_dir.parent.parent.iterdir():
    if path_.is_dir():
        print(path_.name)

print('-' * 80)
# get data from lesson_04
lesson_folder_full_path = str(current_dir.parent)
full_path_to_lesson_04_folder = os.path.join(lesson_folder_full_path, 'lesson_04')

for path_ in pathlib.Path(full_path_to_lesson_04_folder):
    if path_.is_file():
        print(path_.name)

print('-' * 80)

for path_ in current_dir.parent.parent.iterdir():
    if path_.is_dir():
        print(path_.name)
