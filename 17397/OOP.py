class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        print(self.width * self.height)

rect = Rect(100, 100)
rect.get_area()
rect.get_perimeter()
