class User:

    def __init__(self, name: str, score: int):
        self.name = name
        self.score = score

    def __str__(self):
        return f'User: name = {self.name}, score = {self.score} '

    def __setattr__(self, key, value):
        if key == 'score':
            if not (100 >= value >= 0):
                print(f'score mist be between 0 and 100. Set 0')
            value = 0
        super().__setattr__(key, value)  # call __setattr__ from parent class


den = User('Den', -5)
print(den)
