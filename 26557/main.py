# int()
# str()
# float()

# 1+5
# 5-3
# 1*2
# 2/4

# print(2**3) # степень
# print(2//3) # целая часть от деления
# print(5%2) # остаток от деления


# age = int(input('Сколько вам лет: '))
# print('через 10 лет вам будет ' + str(age + 10) + ' лет')
# print(f'Через 10 лет вам будет {age+10} лет')


a = 5
b = 2
print(a==b)
print(a!=b)
print(a>b)
print(a>=b)
print(a<b)
print(a<=b)

# israin = True

# if not israin:
#     print('Пойду гулять!')
# elif israin=='123':
#     print('...')
# else:
#     print('Гулять не пойду')

login = '1234'
password = 'qwerty123'

login1 = '456'
password1 = 'qwertyqwerty'

user_login = input('Введите логин: ')
user_password = input('Введите пароль: ')


if user_login == login and user_password == password:
    print('Вы вошли в первый аккаунт!')
elif user_login == login1 and user_password == password1:
    print('Вы вошли во второй аккаунт!')
else:
    print('Ошибка введенных данных!')