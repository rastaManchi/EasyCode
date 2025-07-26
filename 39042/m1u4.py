# Напишите программу, которая будет складывать полученные от пользователя числа до тех пор, пока тот не введет -1

# summ = 0
# chislo = int(input('Введите число: '))
# summ += chislo
# while chislo != -1:
#     chislo = int(input('Введите число: '))
#     summ += chislo

number = int(input('введите число: '))

while number != -1:
    if number % 2 == 0:
        print('Четное')
    else:
        print('Нечет')
    number = int(input('введите число: '))