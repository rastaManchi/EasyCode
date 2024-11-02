cups = int(input('Введите кол-во чашек: '))

while cups != -1:
    name = input('Введите имя: ')
    if name == 'Вася':
        print('Васе сегодня кофе нельзя!')
    else:
        floor = int(input('Какой этаж'))
        if (1 <= cups <= 3 and floor <= 100) or (4 <= cups <= 7 and floor <= 50) or (8 <= cups and floor <= 2):
            print('Донесу')
    cups = int(input('Введите кол-во чашек: '))
