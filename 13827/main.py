import random 


def create_card():
    number = random.randint(10, 99)
    while number in cards:
        number = random.randint(10, 99)
    cards.append(number)
    return number


cards = []


def card_expiration(month, year):
    return f'{month}/{year+4}'


for i in range(50):
    create_card()

print(cards)

