# user_password = input('Введите пароль: ')

# while user_password != 'qwerty':
#     print('Неверный пароль')
#     user_password = input('Введите пароль заново: ')
# print('Успешный вход')

sum = 0
num = int(input('Введите число: '))

while num != -1:
    sum += num
    num = int(input('Введите число: '))
print(sum)