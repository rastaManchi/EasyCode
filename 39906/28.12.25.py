class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def get_name(self):
        name = self.__name
        print(name)
        
    def get_age(self):
        age = self.__age
        print(age)
        
    def set_name(self, new_name):
        self.__name = new_name

obj1 = Animal('Мурка', 5)
obj1.get_name()
obj1.set_name('Плюсик')
obj1.get_name()

        
