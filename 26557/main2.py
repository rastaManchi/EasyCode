# while True:
#     password = input('Введите пароль: ')
#     if password == 'qwerty':
#         print('Добро пожаловать!')
#         break
#     else:
#         print('Неправильно!')

##############################

# password = input('Введите пароль: ')

# while password != 'qwerty':
#     print('Неправильно')
#     password = input('Попробуйте снова: ')

# print('Добро пожаловать!')


####################################


# for i in range(10):
#     password = input("Введите пароль: ")
#     if password == 'qwerty':
#         print('Добро пожаловать!')
#         break
#     else:
#         print('Ошибка')

# for i in range(10, 0, -1):
#     print(i)


a = float(input('A: '))
n = int(input('N: '))
print(a**n)

y = 1
for i in range(n):
    y = y * a
print(y)

