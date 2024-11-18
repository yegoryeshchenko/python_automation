class SimpleRangeIterator:

    def __init__(self, max_number):
        self.__current = 0
        self.max_number = max_number

    def __iter__(self):
        return self

    def __next__(self):
        if self.__current == self.max_number:
            raise StopIteration

        self.__current = self.__current + 1
        return self.__current


for number in SimpleRangeIterator(15):
    print(number)
