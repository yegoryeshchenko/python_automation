class User:
    def __init__(self, name, password, site_url):
        self.name = name
        self.password = password
        self.site_url = site_url

    def login(self):
        print(f'User {self.name} was logged in {self.site_url}')

    def logout(self):
        print(f'User {self.name} was logged out {self.site_url}')


dev_user = User('dev_user', 'dev_password', 'http://dev-something.org')
stage_user = User('stage_user', 'stage_password', 'http://stage-something.org')
prod_user = User('prod_user', 'stage_password', 'http://prod-something.org')

dev_user.login() # method
dev_user.logout() # method
