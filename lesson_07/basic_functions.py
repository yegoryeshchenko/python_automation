def function_name(params):
    # body
    return ...


function_name([1, 23])

print(len([1, 2, 4]), 'asd', 'cbg', sep="|")


# print(len([1,3,2]), 'asd, 'cbg', sep='|')


def greeting(first_name: str, second_name: str, aka: str) -> str:
    print(f"Hello {first_name.upper()} {second_name.upper()}")


for full_name in [('den', 'mer', 't'), ('alex', 'merson', 's')]:
    greeting(full_name[0], full_name[1], full_name[2])

for full_name in [('den', 'mer', 't'), ('alex', 'merson', 's')]:
    greeting(full_name[0], aka=full_name[2], second_name=full_name[1])

















