# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record to the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result

people_records = [
    ('John', 'Doe', 28, 'Engineer', 'New York'),
    ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
    ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
    ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
    ('Michael', 'Brown', 22, 'Student', 'Seattle'),
    ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
    ('David', 'Miller', 33, 'Software Developer', 'Austin'),
    ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
    ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
    ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
    ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
    ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
    ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
    ('Ava', 'White', 42, 'Journalist', 'San Diego'),
    ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]

print("Task 1 Add your new record to the beginning of the given list")
people_records.insert(0, ('Alex', 'Armstrong', 38, 'Analyst', 'Ohio'))
print(people_records)

print("\nTask 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result")
people_records[1], people_records[5] = people_records[5], people_records[1]
print(people_records)

print("\nTask 3 - check that all people in modified list with records indexes 6, 10, 13 have age >=30. "
      "Print condition check result")

age_criteria = 30
indices = [6, 10, 13]

print("Solution 1:")
is_age_above_30 = True
for k in indices:
    if people_records[k][2] < age_criteria:
        is_age_above_30 = False
        print(f"{people_records[k][0]} {people_records[k][1]}  is younger than 30.")
        break

print("All people at indices [6, 10, 13] have age >= 30:", is_age_above_30)

print("\nSolution 2 - 'all()' function:")

is_all_age_above_30 = all(people_records[k][2] >= age_criteria for k in indices)
print(f"All people at indices [6, 10, 13] have age >= 30: {is_all_age_above_30}")
