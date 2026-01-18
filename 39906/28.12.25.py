# Ранее вы создавали класс Rect с методами, которые вычисляют площадь и периметр фигуры. 
# Наследуйте от данного класса класс Square. Подумайте, какие изменения стоит внести в дочерний класс


class Rect:
    def __init__(self, h, w):
        self.width = w
        self.height = h
        
    def perimetr(self):
        return 0
    
    def area(self):
        return 0
    

class Square(Rect):
    def multipy(self, num):
        self.height *= num 
        self.width *= num
        
    def info(self):
        print('Я квадрат')
        
