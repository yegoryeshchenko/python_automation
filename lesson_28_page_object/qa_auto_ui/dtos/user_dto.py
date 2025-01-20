class UserDTO:
    def __init__(self, first_name: str, last_name: str, email: str, password: str):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self):
        return (f"UserDTO(first_name='{self.first_name}', last_name='{self.last_name}', "
                f"email='{self.email}', password='{self.password}')")
