class BankAccountError(Exception):
    pass


class BankAccount():
    def __init__(self):
        self.__balance = 0
        
        
    def deposit(self, money):
        if money > 0:
            self.__balance += money
        else:
            raise BankAccountError("Нельзя зачислить отрицательное число")
        
        
obj = BankAccount()
obj.deposit(-100)