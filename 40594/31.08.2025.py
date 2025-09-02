import random

def create_card():
    number = random.randint(10000000, 99999999)
    print(f"Номер карты: {number}")

def propper(shvabra):
    print(f"Полы намыты\nШваброй: {shvabra}")

result = 0

def summa(a, b):
    # global result
    result = a + b
    return result


result = summa(2, 5)
print(result)




