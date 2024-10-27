moscow_uch = 2399
moscow_mam = 861
mam_uch = 1744

city1 = input('Введите первый город: ')

if city1 == 'мамадыш':
    city2 = input('Введите второй город: ')
    if city2 == 'москва':
        print(f'{moscow_mam}км между {city1} -- {city2}')
    elif city2 == 'учкудук':
        print(f'{mam_uch}км между {city1} -- {city2}')
    elif city2 == city1:
        print(f'0км между {city1} -- {city2}')

elif city1 == 'учкудук':
    city2 = input('Введите второй город: ')
    if city2 == 'москва':
        print(f'{moscow_uch}км между {city1} -- {city2}')
    elif city2 == 'мамадыш':
        print(f'{mam_uch}км между {city1} -- {city2}')
    elif city2 == city1:
        print(f'0км между {city1} -- {city2}')
        
elif city1 == 'москва':
    city2 = input('Введите второй город: ')
    if city2 == 'учкудук':
        print(f'{moscow_uch}км между {city1} -- {city2}')
    elif city2 == 'мамадыш':
        print(f'{moscow_mam}км между {city1} -- {city2}')
    elif city2 == city1:
        print(f'0км между {city1} -- {city2}')