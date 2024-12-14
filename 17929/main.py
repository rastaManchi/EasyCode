import random 


def summa(a, b):
    result = a + b
    return result

result = 0
result = summa(10, 5)
print(result)

# def create_card():
#     card_number = random.randint(1000000000000000, 9999999999999999)
#     return card_number


# def get_card_end(month, year):
#     end_year = year + 4
#     return f'{month}/{end_year}'


# card_number = create_card()
# card_end_date = get_card_end(12, 2024)
# print(f'Номер карты: {card_number}\nДействует до {card_end_date}')


# def buy(balance, price):
#     if balance >= price:
#         balance -= price
#         return {'status': True, 'new_balance': balance}
#     return {'status': False, 'Error': 'Недостаточно средств!'}


# def check_buy_status(buy_status):
#     if buy_status['status']:
#         print(f'Покупка прошла успешно!\nВаш баланс -- {buy_status["new_balance"]}')
#     else:
#         print(buy_status['Error'])


# buy_status = buy(500, 700)
# check_buy_status(buy_status)

