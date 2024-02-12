class User:
    def __init__(self, name: str, age: int, sex: str, email: str, is_admin: bool):
        self.name = name
        self.age = age
        self.sex = sex
        self.email = email
        self.__is_admin = is_admin

user1 = User('ntn', 52, 'male', 'ntnpub@gmail.com', True)


print(user1.name, user1.age, user1.sex, user1.email, user1._User__is_admin)

