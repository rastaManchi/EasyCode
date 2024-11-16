import os

if os.path.exists('123.txt'):
    file = open('123.txt', 'r', encoding='UTF-8')
else:
    print('Файл не найден!')

