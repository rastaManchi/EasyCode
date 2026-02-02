import random


# random.random()
# random.uniform(1, 10)
# random.randint(1, 10)
# random.randrange(1, 10, 2)

# list_ = [1,2,3,4,5,6,7,8,9]
# random.choice(list_)
# random.shuffle(list_)

summa = 0
command = input("хотите продолжить игру")

while command != "не хочу":
    m = random.randint(1, 6)
    summa += m
    command = input("хотите продолжить игру")
    print(summa)