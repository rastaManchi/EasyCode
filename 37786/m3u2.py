# sword = ['Владислав', 100, 50, 5]

sword2 = {
    'name': 'Владислав',
    'hp': 100,
    'damage': 50,
    'luck': 5
}

print(sword2['name'])
sword2['luck'] = 'Бесконечно'
print(sword2)
sword2['armor'] = 20
print(sword2)

# if 'damage' in sword2:
#     del sword2['damage']
#     print('Элемент удален')
# else:
#     print('Элемента нет')
# print('HA'*100)

slides = {
    'Детская': 5,
    'Зактное солнце': 20,
    'Жираф': 31,
    'Красный дракон': 53,
    'Кантемир': 100
}

for slide in slides:
    print(slide, slides[slide])

for key, value in slides.items():
    print(key, value)
    
slides.keys() # ['Детская', 'Зактное солнце', ...]
slides.values() # [5, 20, 31 ...]

# del slides['Жираф']
# name = input('Введите название новой горки: ')
# length = int(input('Введите длину новой горки: '))
# slides[name] = length
# print(f"{slides['Жираф']}")
