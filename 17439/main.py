cups = int(input('Сколько чашек: '))
floor = int(input('Какой этаж: '))

while cups >= 0:
    if (1<=cups<=3 and floor <= 100) or (4<=cups<=7 and floor <= 50) or (cups>=7 and floor <=2):
        print('Заказ выполнен!')
    else:
        print('Доставку сделать не получится')
    cups = int(input('Сколько чашек: '))
    floor = int(input('Какой этаж: '))