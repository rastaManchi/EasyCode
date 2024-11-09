# amount = int(input('Сколько человек придет? '))

# for i in range(amount):
#     name = input('Введите свое имя: ')
#     print(f'Добрый вечер, {name}')

#  ##########################
# print(2+3+4+5+6+7)

# total = 0

# for i in range(2, 8):
#     print(f'{total} + {i} = {total+i}')
#     total += i

# print(total)
#  ##########################

# for i in range(1, 21, 2):
#     print(i)
#  ###########################

# for i in 'Булат', 'Артем':
#     print(i)
#  ###########################
# forbidden_symbols = "!@#$%^&*()-_=+"
# login = input('Введите логин: ')
# for sym in forbidden_symbols:
#     if sym in login:
#         print(f'{sym} нельзя использовать!')

 ############################

alp = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
step = int(input('Какой шаг? '))
message = input('Введите сообщение: ')
encoded = ''

for sym in message:
    index = alp.find(sym)
    new_index = index + step
    encoded += alp[new_index]

print(encoded)
