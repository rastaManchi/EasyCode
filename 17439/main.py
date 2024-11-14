# promo = 'useless'
# for i in range(3):
#     name = input('Введите имя: ')
#     print(f'{name}, ваш промокод: {promo}')


# for symbol in 'Булат':
#      print(symbol)

alp = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
step = int(input('Введите шаг: '))
message = input('Введите сообщение: ')
encoded = ''

for symbol in message:
    index = alp.find(symbol)
    new_index = index - step
    encoded += alp[new_index]

print(encoded)
