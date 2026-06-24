mnozh = set()

mnozh.add(5)
mnozh.add(6)

mnozh.discard(5)

a = {1, 2, 3}
b = {4, 5, 6, 1}
b.union(a)
b.intersection(a)
b.symmetric_difference(a)
b.difference(a)
a.difference(b)

num1 = input('Введите число: ')
num2 = input('Введите число: ')
symbols1 = set(num1)
symbols2 = set(num2)
print(symbols1.intersection(symbols2))

# num = input('Введите числа через запятую: ') # 1,2,3,4,5,6
# mnozh = set()
# for symbol in num:
#     mnozh.add(symbol)
# mnozh.discard(',')
# print(mnozh)

# num = input('Введите числа через запятую: ') # 1, 2, 3, 4, 5, 6
# num_list = num.replace(' ', '').split(',') # [1,2,3,4,5,6]
# mnozh = set(num_list)
# print(mnozh)