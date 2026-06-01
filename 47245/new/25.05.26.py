# a = 10
# print(a)
# 10 -> int | int()
# 10.0 -> float | float()
# "10" -> str | str()
# True/False -> bool | bool()

# int("10") # 10 | str -> int
# float("10") # 10.0 | str -> float
# str(10) # "10" | int -> str

# num = int(input('Введите число: '))
# print(num + 10)
# print(type(num))

# Операторы сравнения: < | > | <= | >= | != | ==
# Условные операторы: if | elif | else
# Логические операторы: or (или) | and (и) | not
speed = int(input('Введите скорость автомобиля: '))
if speed <= 80:
    print("Не нарушает")
elif speed > 80:
    print('Нарушает')
