import random
import time
from data import *


def fight(enemy_index):
    time.sleep(1)
    round = random.randint(1, 2)
    enemy = enemies[enemy_index]
    enemy_hp = enemy['hp']
    print(f'{enemy["name"]} говорит: {enemy["script"]}')
    input('Enter, чтобы продолжить')
    while enemy_hp > 0 and player['hp'] > 0:
        time.sleep(1)
        if round % 2 == 1:
            print(f'Игрок: {player["name"]} атакует {enemy["name"]}')
            enemy_hp -= player['attack']
            print(f'{player["name"]} - {player["hp"]}\n{enemy["name"]} - {enemy_hp}')
        else:
            print(f"Враг {enemy['name']} атакует {player['name']}")
            player['hp'] -= enemy['attack']
            print(f'{player["name"]} - {player["hp"]}\n{enemy["name"]} - {enemy_hp}')
        round += 1
    if player['hp'] > 0:
        print(f'{enemy["name"]} говорит: {enemy["win"]}')
        enemy_index += 1
        player['hp'] = 100
    else:
        print(f'{enemy["name"]} говорит: {enemy["loss"]}')
    
    return enemy_index





def training():
    print('Тренируемся')

def shop():
    print('Закупаемся')