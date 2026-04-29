# Уровень  Junior
# Напишите программу, которая записывает стихотворения в файл построчно. Получать строки необходимо от пользователя программы через input() 


file = open('output.txt', 'w', encoding='UTF-8')
while True:
    row = input('Введите строку: ')
    if row == 'все':
        break
    file.write(row + '\n')

