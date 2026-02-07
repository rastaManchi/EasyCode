sum = 0
num = int(input('Введите число: '))

while True:
    if num > 1000000:
        break
    sum += num
    num = int(input('Введите число: '))
print(sum)