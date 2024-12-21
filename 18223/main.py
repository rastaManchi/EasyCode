import random


def get_number():
    number = random.randint(10, 30)
    while number in numbers:
        number = random.randint(10, 30)
    numbers.append(number)
    return number 

numbers = []
for i in range(15):
    get_number()

for card_number in numbers:
    print(card_number, end='\n')