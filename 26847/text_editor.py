# file = open('26847/zadacha.txt', 'r', encoding="utf-8")
# r - read - Чтение
# w - write - Запись с удалением
# a - add - добавление в конец

# print(file.read()) чтение файла
# file.write("Первая строка\n") Записать в файл
# file.write("Вторая строка\n")

# data = file.read()
# lines = data.split('\n')
# print(lines)

# lines = file.readlines()
# print(lines)












#В очередной раз запрограммируем процесс регистрации Вконтакте.
#Спросите у пользователя его никнейм и пароль, сохраните в виде одной строки в файле “users.txt”.

#Протестируйте программу на нескольких пользователях. Важно, чтобы к моменту решения следующей задачи в файле было несколько зарегистрированных пользователей

# login = input('Введите логин: ')
# password = input('Введите пароль: ')

# file = open('26847/users.txt', 'a', encoding='utf-8')
# file.write(f'{login} - {password}\n')
# attemps = 0
# isEnter = False

# while attemps < 3:
#     login = input('Введите логин: ')
#     password = input('Введите пароль: ')
#     file = open('26847/users.txt', 'r', encoding='utf-8')
#     lines = file.read().split('\n')
#     for line in lines:
#         info = line.split(' - ')
#         if login == info[0] and password == info[1]:
#             isEnter = True
#             attemps = 3
#             break
#     attemps += 1
#     if not isEnter:
#         print(f'Неверный логин или пароль, у вас осталось {3-attemps} попыток!')       


# if isEnter:
#     print('Успешный вход!')
# else:
#     print('Попробуйте позже!')

import os

if os.path.exists('26847/users.txt'):
    file = open('26847/users.txt', 'r', encoding='utf-8')
else:
    print('Файла не существует!')
