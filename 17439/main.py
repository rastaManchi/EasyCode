slides = {'Детская': 5, 'Закатное солнце': 20, 'Жираф': 31, 'Красный дракон': 53, 'Кантемир': 100}


for slide_name_key, slide_length_value in slides.items():
    print(f'Горка {slide_name_key} -- {slide_length_value}')


print(list(slides.items()))
print(list(slides.keys()))
print(list(slides.values()))
# for key, value in slides.items():
#     print(key, value)

# del slides['Жираф']

# name = input('Введите название новой горки: ')
# метры = input('Введите длину горки: ')

# slides[name] = метры


# slide_name = input('Введите название горки, которую хотите посетить: ')
# while slide_name != 'stop':
#     if slide_name in slides:
#         print(f'Протяженность горки {slide_name} составляет {slides[slide_name]} метр(а\ов)')
#     else:
#         print('Такой горки нет! ')
#     slide_name = input('Пойдем на другую?: ')