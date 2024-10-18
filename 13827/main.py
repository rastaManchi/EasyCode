names = ['Кастрюля', 'Тарелка', 'Ноутбук']
prices = [500, 300, 100000]

for i in range(len(names)):
     print(f'{names[i]} -- {prices[i]}')
    
products = {'Кастрюля':500, 'Тарелка':300, 'Ноутбук': 10000, 'Пылесос': 999999}
products['Кастрюля'] = 1000
products['Утюг'] = 3000
del products['Кастрюля']
print(products)

if 'Пылесос' in products:
    print(products['Пылесос'])
    del products['Пылесос']

#1
slides = {'Десткая': 5, 'Закатное солнце': 20, 'Жираф': 31, 'Красный дракон': 53, 'Кантемир': 100}
#2
del slides['Жираф']
name = input('Введите название горки: ')
length = int(input('Введите длину горки: '))
slides[name] = length
#3
slide_name = input('Какая горка вас интересует? ')
while slide_name != 'stop':
    if slide_name in slides:
        print(f'Протяженность горки "{slide_name}" состовляет {slides[slide_name]} метр(а/ов) ')
    elif slide_name == 'add':
        new_name = input('Введите название горки: ')
        if new_name not in slides:
            slides[new_name] = int(input('Введите протяженность: '))
    elif slide_name == 'delete':
        del_name = input('Введите название горки: ')
        if del_name in slides:
            del slides[del_name]
    elif slide_name == 'all':
        print(slides)
    else:
        print('Такой горки нет!')
    slide_name = input('Какая горка вас интересует? ')

products = {'Кастрюля':500, 'Тарелка':300, 'Ноутбук': 10000, 'Пылесос': 999999}


# for key in products:
#     print(f'{key} -- {products[key]}')

for key, value in products.items():
    print(f'{key} -- {value}')

print(list(products.keys()))
print(list(products.values()))


slides = {'Десткая': 5, 'Закатное солнце': 20, 'Жираф': 31, 'Красный дракон': 53, 'Кантемир': 100}

names = list(slides.keys())
names.sort()
for name in names:
    print(f'{name} -- {slides[name]}')
