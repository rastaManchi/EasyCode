number = int(input('введите число: '))

while number != -1:
    if number % 2 == 0:
        print('Четное')
    else:
        print('Нечетные')
    number = int(input('введите число: '))