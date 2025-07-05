name = "EasyCode" # string
age = 23 # integer
height = 173.5 # float
isadmin = True # boolean

a = 5
b = 2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b) # a в степени b
print(a//b) # целая часть от деления
print(a%b) # остаток от деления

a += 1 
a -= 1
a *= 2
a /= 2
a %= 2
a //= 2

int('23') # '23' -> 23
str(23) # 23 -> '23'
float(23) # 23 -> 23.0

age = input('Введите свой возраст: ')
int_age = int(age)
print('Через 10 лет вам будет', int_age+10, 'лет')