class People:
    def __init__(self,name,age,height,nationality):
        self.name = name
        self.age = age
        self.height = height
        self.nationality = nationality
        
    def __str__(self):
        return f"{self.name, self.age, self.height, self.nationality}"

name_people = str(input("Введите имя: "))
age_people = int(input("Введите возраст: "))
height_people = float(input("Введите ваш рост: "))
nationality_people = str(input("Введите откуда вы: "))

human = People(name_people,age_people,height_people,nationality_people)

name_people = str(input("Введите имя: "))
age_people = int(input("Введите возраст: "))
height_people = float(input("Введите ваш рост: "))
nationality_people = str(input("Введите откуда вы: "))

human2 = People(name_people,age_people,height_people,nationality_people)

print(human)