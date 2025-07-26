# age = str(input('Возраст: '))
10 # integer
10.0 # float 
True # boolean
'Булат' #string
# +
# -
# /
# *
# //
# %
# **

# >
# <
# ==
# !=
# >=
# <=
# password_user = input('Пароль:')
# password = 'qwerty'
# password2 = '12345'
# if password == password_user:
#     print('Вы вошли')
# elif password2 == password_user:
#     print('Вы вошли во второй аккаунт!')
# else:
#     print('Ошибка')

# names = ['Вадим', 'Булат', 'sdmgvfjksdfvb']
# # print(names[0:2])
# # names.append('Коля')
# # names.remove('Булат')
# # names.pop(0)
# # print(names)
# names[1] = 'Глеб'

# users = [
#     {
#         'name': 'Булат',
#         'surname': 'Закиров'
#     },
#     {
#         'name': 'Вадим',
#         'surname': 'Рубцов'
#     }
# ]

# for user in users:
#     print(f'{user["name"]} -- {user["surname"]}')

# age = 23

# def after10(age_local):
#     age_local+=10
#     return age_local
    
# age = after10(age)
# print(f'Вам через 10 лет будет: {age} лет')
        
        
class Car:
    def __init__(self, mark, model, color, price, mileage):
        self.mark = mark
        self.model = model
        self.color = color
        self.price = price
        self.mileage = mileage
        
    def drive(self, miles):
        self.mileage += miles
        print(f'{self.mark} проехал(а) {miles}км. Общий пробег: {self.mileage}')
        
    def __str__(self):
        return f'\nМарка: {self.mark}\nМодель: {self.model}\n\n'
    

class ElectricCar(Car):
    def __init__(self, mark, model, color, price, mileage, battery):
        super().__init__(mark, model, color, price, mileage)
        self.battery = battery
         
        
car1 = Car('Тойота', 'Камри', 'черный', 2500000, 2000)
car2 = ElectricCar('Тесла', 'Plait', 'черный', 5000000, 1000, 100)

car1.drive(100)
car2.drive(500)

print(car1)
print(car2)