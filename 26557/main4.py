class Car:
    def __init__(self, name, color, mileage):
        self.name = name
        self.color = color
        self.mileage = mileage

    def move(self, miles):
        self.mileage += miles

    def __str__(self):
        return f'Марка: {self.name} -- Цвет: {self.color} -- Километраж: {self.mileage}'

car1 = Car('Ford', 'Black', 15000)
car2 = Car('Nissan', 'Blue', 0)

car2.move(20)

print(car2)
print(car1)