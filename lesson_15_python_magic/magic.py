class User:
    def __init__(self, name, password, site_url, height=175):
        self.name = name
        self.password = password
        self.site_url = site_url
        self.finished_courses = []
        self.height = height

    def login(self):
        print(f'User {self.name} was logged in {self.site_url}')

    def logout(self):
        print(f'User {self.name} was logged out {self.site_url}')

    def __len__(self):  # при виклику str
        return len(self.height)

    def __eq__(self, other):
        return self.height == other.height

    def __str__(self):
        return f'user: {self.name}, url: {self.site_url}'

    def __repr__(self):
        return f'user: {self.name}, surname {self.password}, url: {self.site_url}'


den = User('Den', "123", 'google', 176)
max = User('Den', "123", 'google')

print(den.__eq__(max))



st = User('Yehor', 'Yeshchenko', 'google.com')
print(str(st))
print(repr(st))

st.finished_courses.append('math')
st.finished_courses.append('phil')

