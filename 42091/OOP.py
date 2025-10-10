class Rect:
    def __init__(self, shirina, visota):
        self.width = shirina
        self.height = visota
    def get_area(self):
        return self.width * self.height
    def get_perimeter(self):
        return self.width * 2 + self.height * 2
    
r = Rect(20, 5)
print(r.get_area())
print(r.get_perimeter())
r2 = Rect(10, 5)
print(r2.get_area())
print(r2.get_perimeter())















