users = [
    {'name': 'den', 'math': 50, 'phil': 60},
    {'name': 'den1', 'math': 50, 'phil': 60},
    {'name': 'den2', 'math': 50, 'phil': None}
]


def test_count_data(user_list):
    for k in user_list:

        try:

            assert k['math'] + k['phil'] > 0
            print(k['name'], k['math'], + k['phil'])

        except KeyError as asd:

            print(f"Cat get correct data for {k}")
            raise asd

        except TypeError:

            print(f"found none, not a bug, continue")


test_count_data(users)
