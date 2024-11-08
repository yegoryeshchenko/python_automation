class Classes:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


    def __add__(self, obj):
        for k, v in obj.items():
            setattr(self, k, v)


    # def __str__(self):
    #     res =

basic_classes = Classes(**{
    'math': {'hours': 100, 'students':20, 'start': '20.05.2024'},
    'phil': {'hours': 100, 'students':20, 'start': '21.05.2024'},
})

extra_classes = Classes(**{
    'biology': {'hours': 40, 'students':20, 'start': '20.05.2024'},
})
