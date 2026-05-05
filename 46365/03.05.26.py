class Animal:
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        print(f"{self.name} издает звук")

class Dog(Animal):
    def sound(self):
        print(f"Собачка {self.name} говорит: Гав-гав!")

class Cat(Animal):
    def sound(self):
        print(f"Кошка {self.name} говорит: Мяу!")

class Cow(Animal):
    def sound(self):
        print(f"Корова {self.name} говорит: Муу!")
        
        
animals = []
animals.append(Dog('Михалыч'))
animals.append(Cat('Дымочек'))
animals.append(Cow('Буренка'))

for animal in animals:
    animal.sound()
