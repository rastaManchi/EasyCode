class Rect: 
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.height*self.height
    
    def get_perimetr(self):
        return 2*(self.height+self.width)
    

r1 = Rect(100, 30)
r1_area = r1.get_area()
r1_perimetr = r1.get_perimetr()

print(f'Площадь: {r1_area}\nПериметр: {r1_perimetr}')
