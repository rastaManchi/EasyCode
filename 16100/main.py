floor = int(input('введите этаж: '))
water = int(input('Сколько литров: '))


if (floor <= 53 and water <= 5) or (floor <= 99 and water <= 2) or (floor <= 100 and water <= 1):
    print('Сможет!')
else:
    print('не сможет!')

