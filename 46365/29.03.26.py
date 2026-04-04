import random 

random.random()
random.randint(1, 3)
random.uniform(1, 3)
random.randrange(1, 10, 2)


list_ = ['орел', 'решка']
random.choice(list_)
random.shuffle(list_)


import random

kubik=[1, 2, 3, 4, 5, 6]

rpndom=(random.choice(kubik))
print(rpndom)
d = input("хотите перебрасать?: ")
if d == "кнш":
    rpndom=(random.choice(kubik))
    print(rpndom)
