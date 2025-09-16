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
    type = input('Что мы тренируем?\n1 - Атака\n2 - Оборона\n')
    for procent in range(0, 101, 10):
        print(f"Тренировка завершена на {procent}%")
        time.sleep(1)
    if type=='1':
        player['attack'] += 5
    else:
        player['armor'] += 5

def shop():
    msg = ""
    count = 1
    for item in shop_items:
        msg += f"{count} - {item['name']} - {item['price']}\n"
        count += 1
    print(msg)
    user_chioce = int(input('Какой товар выберите: ')) - 1
    if player['money'] >= shop_items[user_chioce]['price']:
        player['money'] -= shop_items[user_chioce]['price']
        player['inventory'].append(shop_items[user_chioce])
    else:
        print('Денег нет')
    print(player['inventory'])
    print(player['money'])
