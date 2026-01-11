# for row in range(1, 10):
#     for column in range(1, 10):
#         print(str(row * column).ljust(5), end=' ')
#     print()



# В 7Б классе проходят тему простые числа.
# Скоро контрольная и Анатолий решил,
# что нужно написать программу, которая вычислит все простые числа от a до b

a = int(input('Введите число: '))
b = int(input('Введите число: '))

for num in range(a, b+1):
    is_easy = True
    for i in range(2, num):
        if num % i == 0:
            is_easy = False
    if is_easy:
        print(num)



