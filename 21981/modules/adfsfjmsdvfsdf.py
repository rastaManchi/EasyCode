class Player():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def add_age(self, other):
        return self.age  + other

    def __add__(self, other):
        return self.age + other

    def __mul__(self, other):
        return self.age * other

    def __str__(self):
        return f"\n\nИмя: {self.name}\nВозрат: {self.age}"
    

