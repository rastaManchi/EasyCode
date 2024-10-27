age = int(input('Введите свой возраст: '))

if age >= 16:
    login = input('Введите логин: ')
    password = input('Введиет пароль:')
    if login == '123' and password == 'qwerty':
        print('Вы вошли!')
    else:
        print('Ошибка доступа!')
elif age >= 1 and age <= 15:
    print('Подрасти сначала!')
else:
    print('Ты кто?')

