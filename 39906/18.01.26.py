# Создайте абстрактный класс Vehicle, который имеет абстрактные методы start_engine(),
# stop_engine() и fuel()
# Реализуйте несколько подклассов: Car, Motorcycle и Bicycle

# Для методов start и stop_engine необходимо просто вывести соответствующую фразу, а вот для метода fuel() рассчитать стоимость топлива по формуле:
# Для машины (Car) топливо стоит 72 за ед.
# Для мотоцикла (Motorcycle) топливо стоит 52 за ед.
# Для велосипеда топливо не нужно
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    
    @abstractmethod
    def stop_engine(self):
        pass
    
    @abstractmethod
    def fuel(self, volume):
        pass
    
    
class Car(Vehicle):
    def start_engine(self):
        print('Двигатель запущен!')
        
    def stop_engine(self):
        print('Дигатель остановлен!')
        
    def fuel(self, volume):
        print(f"На топливо было потрачено {72 * volume}р.")
        

class Motorcycle(Vehicle):
    def start_engine(self):
        print('Двигатель запущен!')
        
    def stop_engine(self):
        print('Дигатель остановлен!')
        
    def fuel(self, volume):
        print(f"На топливо было потрачено {52 * volume}р.")
        
        
class Bicycle(Vehicle):
    def start_engine(self):
        print("Сели на велик")
        
    def stop_engine(self):
        print("Слезли с велика")
        
    def fuel(self, volume=None):
        print("Заправка невозможна")
        
        
car = Car()
motorcycle = Motorcycle()
bike = Bicycle()

car.start_engine()
motorcycle.start_engine()
bike.start_engine()

car.stop_engine()
motorcycle.stop_engine()
bike.stop_engine()

car.fuel(10)
motorcycle.fuel(10)
bike.fuel(10)
        