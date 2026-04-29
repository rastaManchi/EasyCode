class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def go_to_wc(self):
        print(f"{self.name} сходил в туалет")
        
    def greetings(self):
        print(f"привет, меня зовут {self.name}, мне {self.age}")
        
# people1 = People('Булат', 24)
# people2 = People('Саид', 15)

# people1.go_to_wc()
# people2.greetings()


class Cat:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        
    def __str__(self):
        return f'{self.name} - {self.gender} - {self.age}'
    

        
        
cat1 = Cat('nsdl,fsd', 'м', 3)
print(cat1+2134)