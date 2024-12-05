import json


users_data = [
    {'id': 1, 'is_active': True, 'friends': None, 'name': 'Ivan'},
    {'id': 1, 'is_active': True, 'friends': None, 'name': 'Ivan'},
    {'id': 1, 'is_active': True, 'friends': [
        {'id': 1, 'is_active': True, 'friends': None, 'name': 'Ivan'}],
     'name': 'Ivan'},
]

users_data_json = json.dumps(users_data)  # створення json формату, повертає str

# with open('json_as_str.txt', 'w') as f
#     f.write(users_data_json)
#
# with open('json_as_json.json' ,'w') as f:
#     json.dump(users_data, f, indent=4)

with open('json_as_str.txt') as f:

    data = json.loads(f.read())

with open('json_as_str.txt') as f:

    data2 = json.load(f)

print(data)
print(data2)

