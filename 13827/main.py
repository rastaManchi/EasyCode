HP_Player = 100
HP_NPS = 100

import random

Fire = random.randint(15,30)
Ice = 20
Iand = 5

while HP_Player > 0 and HP_NPS > 0:
    Atak = random.randint(0, 1)
    if Atak == 0:
        print('Атаку проводит Player')
        Atak2 = random.randint(1,3)
        if Atak2 == 1:
            print('Огонь')
            HP_NPS -= Fire
        elif Atak2 == 2:
            print('Лед')
            HP_NPS -= Ice
        else:
            print('Земля')
            HP_NPS -= Iand
    else:
        print('Атаку проводит враг')
        Atak2 = random.randint(1,3)
        if Atak2 == 1:
            print('Огонь')
            HP_Player -= Fire
        elif Atak2 == 2:
            print('Лед')
            HP_Player -= Ice
        else:
            print('Земля')
            HP_Player -= Iand
    