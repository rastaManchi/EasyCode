class Rectangle:  
    def __init__(self, width, height):  
        self.width = width  
        self.height = height  
  
    def area(self):  
        """Вычисляет площадь прямоугольника"""  
        return self.width * self.height  
  
    def perimeter(self):  
        """Вычисляет периметр прямоугольника"""  
        return 2 * (self.width + self.height)  
  
  
class Circle:  
    def __init__(self, radius):  
        self.radius = radius  
        self.pi = 3.14159  
  
    def area(self):  
        """Вычисляет площадь круга"""  
        return self.pi * (self.radius ** 2)  
  
    def perimeter(self):  
        """Вычисляет длину окружности"""  
        return 2 * self.pi * self.radius  
  
  
class Triangle:  
    def __init__(self, a, b, c):  
        self.a = a  
        self.b = b  
        self.c = c  
  
    def area(self):  
        """Вычисляет площадь треугольника по формуле Герона"""  
        s = self.perimeter() / 2  
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5