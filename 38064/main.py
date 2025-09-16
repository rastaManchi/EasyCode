[] # список
() # кортеж
{} # словарь

pirates = []

command = input('Введите команду: ')

while command != 'stop':
    if command == '1':
        name = input('Введите имя пирата: ')
        age = int(input('Введите возраст пирата:'))
        special = input('Введите специальность пирата: ')
        pirates.append({
            "name": name,
            "age": age,
            "special": special
        })
    elif command == '2':
        del_name = input('Введите Имя пирата: ')
        for pirate in pirates:
            if pirate['name'] == del_name:
                pirates.remove(pirate)
    elif command == '3':
        print(pirates)
    else:
        print('Такой команды нет')
    
    command = input('Введите команду: ')




