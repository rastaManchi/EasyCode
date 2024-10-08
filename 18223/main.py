import random

dice = input('Сколько граней на кубе? ')
dice = int(dice)

result = random.randint(1, dice)
print(result)