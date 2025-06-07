from bs4 import BeautifulSoup as bs
import warnings

   
count = 0
width = 0
result = ''
for i in range(0, 106):
    if i < 10:
        file = open(f'0601(3)_000/0601(3)_00{i}.svg', 'r', encoding='utf-8')
    elif i < 100:
        file = open(f'0601(3)_000/0601(3)_0{i}.svg', 'r', encoding='utf-8')
    else:
        file = open(f'0601(3)_000/0601(3)_{i}.svg', 'r', encoding='utf-8')
    data = bs(file.read(), 'lxml').find('g')
    data['transform'] = f'translate({width}.000000,1080.000000) scale(0.100000,-0.100000)'
    result += str(data)
    width += 1920

new_file = open('new.svg', 'w', encoding='utf-8')
new_file.write(result)
