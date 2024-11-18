# Завдання 1
#
# Створіть клас Employee, який має атрибути name та salary. Далі створіть два класи, Manager та Developer,
# які успадковуються від Employee. Клас Manager повинен мати додатковий атрибут department,
# а клас Developer - атрибут programming_language.
#
# Тепер створіть клас TeamLead, який успадковується як від Manager, так і від Developer.
# Цей клас представляє керівника з команди розробників. Клас TeamLead повинен мати всі атрибути як Manager
# (ім'я, зарплата, відділ), а також атрибут team_size, який вказує на кількість розробників у команді, якою керує керівник.
#
# Напишіть тест, який перевіряє наявність атрибутів з Manager та Developer у класі TeamLead

import pytest


class Employee:
    def __init__(self, name: str, salary: int):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name: str, salary: int, department: str):
        Employee.__init__(self, name, salary)
        self.department = department

    def __str__(self):
        return f'Manager - name {self.name}, salary: {self.salary}, department: {self.department}'


class Developer(Employee):
    def __init__(self, name: str, salary: int, programming_language: str):
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language

    def __str__(self):
        return f'Developer - name {self.name}, salary: {self.salary}, programming_language: {self.programming_language}'


class TeamLead(Manager, Developer):
    def __init__(self, name: str, salary: int, department: str, team_size: int, programming_language: str):
        super().__init__(name, salary, department)
        self.programming_language = programming_language
        self.team_size = team_size

    def __str__(self):
        return f'TeamLead - name {self.name}, salary: {self.salary}, department: {self.department}, ' \
               f'programming_language: {self.programming_language}, team_size: {self.team_size}'


manager = Manager('Petro', '1550', 'Ecommerce')
print(manager)
developer = Developer('Ivan', '1500', 'Java')
print(developer)

team_lead = TeamLead('Roman', '1600', 'Insurance', 5, '.NET')
print(team_lead)


@pytest.mark.parametrize("attribute",
                         ['department',
                          'programming_language'])
def test_team_lead_object_should_have_attributes_from_manager_and_developer(attribute):
    mykola_team_lead = TeamLead("Mykola", "1800", "Ecommerce", 20, "Python")

    assert hasattr(mykola_team_lead,
                   attribute), f"Team lead should have attribute '{attribute}'"
