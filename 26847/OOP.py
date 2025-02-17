class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height
    
    def get_perimetr(self):
        return 2 * (self.width + self.height)
    

rect = Rect(100, 100)
print(rect.get_area())
print(rect.get_perimetr())