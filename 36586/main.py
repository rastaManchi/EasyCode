class Item():
    def __init__(self):
        self.age = 16
    
    def __str__(self):
        return f"{self.age}"
    
obj = Item()
print(obj)