place = [
    ['*', '*', '*'],
    ['*', '*', '*'],
    ['*', '*', '*'],
]

def print_place():
    for row in place:
        print('|'.join(row))
    print()

turn = 1
while True:
    row = int(input('Строка: '))
    column = int(input('Колонка: '))
    if turn % 2 == 0:
        place[row-1][column-1] = 'O'
    else:
        place[row-1][column-1] = 'X'
    print_place()
    #TODO: проверка победы
    turn += 1
    