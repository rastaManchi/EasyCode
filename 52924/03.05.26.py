a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
result = ''


for number in range(a, b+1):
    status = True
    for i in range(2, number):
        if number % i == 0:
            status = False
            break
    if status:
        result += str(number) + ', '
        
print(result)
     
