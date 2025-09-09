fruits = ('Яблоко', 'Банан')

name = input('Введи название фрукта: ')

count = 1

for i in fruits:
    if name == i:
        result = count
    count += 1

print(f'{name} - фрукт под номером {result}')