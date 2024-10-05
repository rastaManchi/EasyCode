import random

hp = 100


while hp > 0:
    for i in range(5):
        hp -= random.randint(1, 10)
    print(hp)

print(hp)
