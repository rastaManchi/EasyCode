# user_password = input('Введите пароль: ')

# while user_password != 'qwerty':
#     print('Неверный пароль')
#     user_password = input('Введите пароль заново: ')
# print('Успешный вход')

# while True:
#     user_password = input('Введите пароль: ')
#     if user_password == 'qwerty':
#         print('Успешный вход')
#         break
#     print('Неверный пароль')

deliteli = ""
current_delitel = 2
num = int(input('Введите число: '))


while current_delitel <= num:
    if num % current_delitel == 0:
        deliteli += f" {current_delitel},"
        break
    current_delitel += 1
print(deliteli)
