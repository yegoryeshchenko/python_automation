import pathlib
import sys

# pathlib - шлях до поточного файлу
# sys.path - шлях до поточного файлу
print(f'file path: {pathlib.Path(__file__)}')
sys.path.insert(0, str(pathlib.Path(__file__().parent.parent.parent)))

x = pathlib.Path(__file__)
