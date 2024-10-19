class User:
    def __init__(self, name, login, password):
        self.name = name
        self.login= login
        self.password = password

    def hello(self):
        print(f"Приветствую! Меня зовут {self.name}")


user2 = User('Кирилл', 'login2', 'qwerty123')
user = User('Булат', 'login', 'qwerty')


user2.hello()