# В аквапарке сотрудники никак не могут запомнить,
# какая протяженность у их горок - а посетители постоянно спрашивают. 
# Создайте словарь, в котором будут храниться пары название - 
# протяженность. Вот какие есть горки:

# Детская - 5 метров
# Закатное солнце - 20 метров
# Жираф - 31 метр
# Красный дракон - 53 метра
# Кантемир - 100 метров

slides = {
    'Детская': 5,
    'Закатное солнце': 20,
    'Жираф': 31,
    'Красный дракон': 53,
    'Кантемир': 100
}

# На горку “Жираф” поступало больше всего жалоб - говорят, 
# совсем на жирафа не похожа. Надо её чем-нибудь заменить.
# Напишите программу, которая удалит из словаря горку “Жираф”, 
# спросит у администратора аквапарка название новой горки 
# и её протяженность и добавит новую пару в словарь

del slides['Жираф']
slide_name = input('Введите название новой горки: ')
slide_dist = int(input('Введите протяженность новой горки: '))
slides[slide_name] = slide_dist
print(list(slides.items())) # .items()
print(list(slides.keys()))  # .keys()
print(list(slides.values())) # .values()
