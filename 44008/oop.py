# Добавьте в класс Rect два метода: get_area(self), 
# возвращающий площадь прямоугольника, и get_perimeter(self), возвращающий его периметр




class Rect:
    def __init__(self, height, width): 
        self.height = height
        self.width = width

    def get_perimeter(self):
        return 2*(self.height + self.width)
    
    def get_area(self):
        return self.width * self.height
    
object_ = Rect(120, 100)
result = object_.get_perimeter()
result2 = object_.get_area()
print(result)