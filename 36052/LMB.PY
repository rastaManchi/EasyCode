# c = 1000 # Глобальная

# def summa(local_c):
#     local_c += 1
#     return local_c
    
# c = summa(c)
# print(f'Глобальная: {c}')

# c = 10

# def summa():
#     global c
#     c += 1

# summa()
# print(c)

import random

def get_card():
    number = random.randint(1000000, 9999999)
    return number

print(f'Ваш номер карты: {get_card()}')