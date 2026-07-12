class User:
    def __init__(self, login, password):
        # Приватные
        self.__login = login
        self.__password = password
        
        # Защищенные
        self._login = login
        self._password = password
        
        # Публичные
        self.login = login
        self.password = password
        
    def get_password(self):
        return self.__password
        
    def set_password(self, new_password):
        if len(new_password) >= 8:
            self.__password = new_password
        else:
            print('Длина пароля должна быть больше 8 символов')
        
        
obj = User('login123', 'qwerty')
print(obj.get_password())
obj.set_password('12345678')
print(obj.get_password())

