file = open('27278/info.txt', 'r', encoding='utf-8')
name = input()

# r - read only
# w - write only
# a - add only

# print(file.read())
# print(file.write('Герман\n'))

data = file.read()
lines = data.split('\n')
print(lines)



# file = open('27278/users.txt', 'a', encoding='utf-8')
# name = input('Введите свое имя: ')
# password = input('Введите свой пароль: ')
# file.write(f'{name} -- {password}\n')

name = input('ВВедите свое имя: ')
user_password = input('Введите свой пароль: ')

exists = False

file = open('27278/users.txt', 'r', encoding='utf-8')
data = file.read()
users = data.split('\n')
for user in users:
    login, password = user.split(' -- ')
    if name == login and user_password == password:
        print('Добро пожаловать!')
        exists = True
        break
    elif name==login and user_password != password:
        print('Пароль неверный!')
        exists = True
        break

if not exists:
    print('Пользователя не существует!')

