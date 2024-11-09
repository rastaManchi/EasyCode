from data import *
from random import randint
from time import sleep


name = input('Введи своё имя, путник: ')
player['name'] = name
current_enemy = 0


round = randint(1, 2)
enemy = enemies[current_enemy]
enemy_hp = enemies[current_enemy]['hp']
print(f'Противник - {enemy["name"]}: {enemy["script"]}')
input('Enter чтобы продолжить')
print()

while player['hp'] > 0 and enemy_hp > 0:
    if round % 2 == 1:
        print(f'{player["name"]} атакует {enemy["name"]}.')
        enemy_hp -= player['attack']
        sleep(1)
        print(f'''{player['name']} - {player['hp']}
{enemy['name']} - {enemy_hp}''')
        print()
        sleep(1)
    else:
        print(f'{enemy["name"]} атакует {player["name"]}.')
        player['hp'] -= enemy['attack']
        sleep(1)
        print(f'''{player['name']} - {player['hp']}
{enemy['name']} - {enemy_hp}''')
        print()
        sleep(1)
    round += 1

if player['hp'] > 0:
    print(f'Противник - {enemy["name"]}: {enemy["win"]}')
else:
    print(f'Противник - {enemy["name"]}: {enemy["loss"]}')