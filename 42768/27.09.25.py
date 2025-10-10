# >
# <
# >=
# <=
# ==
# != 

# and
# or
# not

# input()
# int()

# if 

# password = input('Введите пароль: ')
# password_repeat = input('Введите пароль снова: ')

# if password==password_repeat:
#     print()
#     print('Регистрация завершена успешно')
#     print()
# print('Программа завершила свою работу.')

# a + b > c
# a + c > b
# b + c > a

# a = 5
# a % 2 == 0



# Примечание:
# Год является високосным, если его номер кратен 4, но не кратен 100, или если он кратен 400

year = int(input('Какой год вас интересует: '))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('+')
else:
    print('-')
