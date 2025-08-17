import time
import random
from data import *

def fight(current_enemy):
    round = random.randint(1, 2)
    enemy = enemies[current_enemy]
    enemy_hp = enemies[current_enemy]['hp']
    print(f'Противник - {enemy["name"]}: {enemy["script"]}')
    input('Enter, чтобы продолжить')
    print()
    while player['hp'] > 0 and enemy_hp > 0:
        if round % 2 == 1:
            print(f'{player["name"]} атакует {enemy["name"]}')
            crit = random.randint(1, 100)
            if crit < player["luck"]:
                enemy_hp -= player["attack"] * 3
            else:
                enemy_hp -= player["attack"]
            time.sleep(1)
        else:
            print(f'{enemy["name"]} атакует {player["name"]}')
            player["hp"] -= enemy["attack"] * player['armor']
            time.sleep(1)
        print(f'''{player["name"]} -- {player["hp"]}
{enemy["name"]} -- {enemy_hp}''')
        print()
        time.sleep(1)
        round += 1
    if player["hp"] > 0:
        print(f'Противник - {enemy["name"]}: {enemy["win"]}')
        current_enemy += 1
    else:
        print(f'Противник - {enemy["name"]}: {enemy["loss"]}')
    player["hp"] = 100
    return current_enemy

def training():
    training_type = input('Какой вид:\n1 - Сила\n2 - оборона\n')
    for i in range(0, 101, 10):
        print(f'тренировка завершена на {i}%')
        time.sleep(1)
    if training_type == '1':
        player['attack'] += 3
    else:
        player['armor'] -= 0.05
    print('Тренировка завершена')