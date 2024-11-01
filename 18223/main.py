mosc_mam = 861
mosc_uch = 2399
mam_uch = 1744


city1 = input('Введите город: ')
city2 = input('Введите город: ')


if city1 == 'Москва':
    if city2 == 'Мамадыш':
        print(mosc_mam)
    elif city2 == 'Учкудук':
        print(mosc_uch)
    elif city2 == city1:
        print(0)
elif city1 == 'Мамадыш':
    if city2 == 'Москва':
        print(mosc_mam)
    elif city2 == 'Учкудук':
        print(mam_uch)
    elif city2 == city1:
        print(0)
elif city1 == 'Учкудук':
    if city2 == 'Мамадыш':
        print(mam_uch)
    elif city2 == 'Москва':
        print(mosc_uch)
    elif city2 == city1:
        print(0)
else:
    print('Ошибка!')
