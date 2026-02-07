age = int(input())

if age >= 13:
    password = input('Введите пароль: ')
    if len(password) >= 8:
        print('Добро пожаловать')
    else:
        print('Длина пароля неверная')
else:
    print('Возраст не подходит')