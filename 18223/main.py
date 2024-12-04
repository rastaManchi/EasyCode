# products_name = ['Кастрюля', 'Ложка']
# price = [500, 100]

# dict_1 = {
#     'Кастрюля':500,
#     'Ложка':100
# }

# print(dict_1['Кастрюля'])

# dict_1['Кастрюля'] = 200

# dict_1['Утюг'] = 1000

# del dict_1['Кастрюля']

# dict_1['Пылесос'] = 99999999

# if 'Пылесос' in dict_1:
#     print(dict_1['Пылесос'])
#     del dict_1['Пылесос']

# print(dict_1)

# dict_1 = {
#     'Кастрюля':500,
#     'Ложка':100
# }


# for key, value in dict_1.items():
#     print(f'{key} -- {value}')


# print(list(dict_1.keys()))
# print(list(dict_1.values()))

slides = {
    'Детская': 5,
    'Закатное солнце': 20,
    'Жираф': 31,
    'Красный дракон': 53,
    'Каньемир': 100
}


# for i in slides:
#     print(f'{i} -- {slides[i]}')


for name, length in slides.items():
    print(f'{name} -- {length}')


del slides['Жираф']

name = input('Введите название новой горки: ')
length = int(input('Введите длину горки: '))

slides[name] = length
print(slides)


name = input('Введите название горки: ')
if name in slides:
    print(f'Протяженность горки”{name}” составляет {slides[name]} метр(а/ов)')
else:
    print('Такой горки нет!')






