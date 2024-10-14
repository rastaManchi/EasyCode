# a = 10
# b = 10

# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)
# print(a == b)
# print(a != b)

floor = int(input('Какой этаж? '))
water = int(input('Сколько литров? '))

if (floor <= 53 and water <= 5) or (floor <= 99 and water <= 2) or (floor <= 100 and water <= 1):
    print('Смогу!')
else:
    print('Не смогу!')
