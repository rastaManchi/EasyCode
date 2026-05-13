class Card():
    def __init__(self, number, gender, balance = 1000):
        self.number = number
        self.__balance = balance # приватный
        # self._balance = balance защищенный
        # self.balance = balance публичный
        self.__gender = gender
        
    def get_balance(self):
        return self.__balance
        
    def set_balance(self, summ):
        if summ > 0:
            self.__balance += summ
        else:
            print('Число должно быть больше 0')
            
    def set_gender(self, new_gender):
        self.__gender = new_gender
        
        
obj = Card('123 123 123', 'м')
print(obj.get_balance())
obj.set_balance(100)
print(obj.get_balance())

obj.set_gender('м')
obj.set_gender('ж')

