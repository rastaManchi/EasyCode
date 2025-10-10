# Напишите программу, которая будет подсчитывать куб и квадрат числа,
# введенного пользователем. Цикл должен завершиться тогда, когда на вход программа получит -1


# while True:
#     number = int(input('Введите число: '))
#     if number == -1:
#         break
#     if number == 0:
#         continue
#     print(number**2)
#     print(number**3)
#     print()

n = int(input("число: "))
count = 0
i = 1

while i <= n:
    if n % i != 0:
        i += 1
        continue
    count += 1
    i += 1
else:
    print(f"количество делителей {n}: {count}")
