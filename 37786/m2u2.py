correct_password = 'easycodeisthebest'
password = input('введите пароль: ')

while password != correct_password:
   password = input('Ошибка!!!\nВведите пароль заново: ')
   
print('Вход в аккаунт выполнен')