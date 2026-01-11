class CustomError(Exception):
    def __init__(self):
        self.message = 'Число меньше нуля'
        super().__init__(self.message)
        
    def __str__(self):
        return self.message
        
    

def check_value(x):
    if x < 0:
        raise CustomError

try:
    check_value()
# Exception
#   ZeroDivisionError
#   ValueError
#   CustomError
except TypeError as e:
    print(f'Ошибка - {e}')
