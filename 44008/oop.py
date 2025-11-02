class Car:
    def __init__(self, model, power, speed, color):
        self.model = model
        self.power = power
        self.speed = speed
        self.color = color
        
    def forward(self):
        print(f'Я еду вперёд со скоростью {self.speed}')
        
    def __str__(self):
        return f"Модель: {self.model}"

car = Car("Supra", 300, 200, 'black')
print(car)