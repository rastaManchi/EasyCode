PI = 3.14
NAME = 'Булат'


def summa(num1, num2):
    print(f"{num1} + {num2} = {num1 + num2}")
    

def racnost(num1, num2):
    print(f"{num1} - {num2} = {num1 - num2}")


def umnozh(num1, num2):
    print(f"{num1} * {num2} = {num1 * num2}")
    
    
def delenie(num1, num2):
    if num2 == 0:
        print("Ошибка: Деление на ноль!")
    else:
        print(f"{num1} / {num2} = {num1 / num2}")