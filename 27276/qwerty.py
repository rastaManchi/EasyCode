class Rectangle:
   def __init__(self, w, h):
       self.width = w
       self.height = h




   def perimeter(self):
       return self.width * 2 + self.height * 2
  


   def area(self):
       return self.width * self.height
   
def print_info(r: Rectangle):
   print(r.perimeter())
   print(r.area())

