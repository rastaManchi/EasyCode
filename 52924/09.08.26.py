import random


print(random.random())
print(random.uniform(1, 10))
print(random.randint(1, 10))
print(random.randrange(1, 10, 5))


LIST_ = [1, 2, 3, 'Булат']
print(random.choice(LIST_))
random.shuffle(LIST_)
print(LIST_)

