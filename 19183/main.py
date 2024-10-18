# 2>5
# 2<5
# 2==5
# 2!=5
# 2>=5
# 2<=5

# age = int(input('Введите ваш возраст: '))
# password = input('Введите ваш пароль: ')
# status = age >= 18 and len(password) >= 6
# print(f'Статус регистрации: {status}')


# ticket = input('У вас есть билет? ')
# age = int(input('Введите ваш возраст: '))
# status = ticket == 'да' or age < 7
# print(f'Статус поездки: {status}')

age = int(input('Введите ваш возраст: '))
password = input('Введите пароль: ')
if age >= 18 and len(password) >= 6:
    print('Успешо!')
else:
    print('Ошибка!')
