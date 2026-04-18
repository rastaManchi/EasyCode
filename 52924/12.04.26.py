age = int(input())

if age > 13:
    password = input()
    if len(password) >= 8:
        print('Добро пожаловать!')
    else:
        print('Длина пароля не подходит')
else:
    print('Возраст не подходит')