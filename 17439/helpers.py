from time import sleep
from random import randint
from data import *


def fight(current_enemy):
    round = randint(1, 2)
    enemy = enemies[current_enemy]
    enemy_hp = enemy['hp']

    print(f'Противник -- {enemy["name"]}: {enemy["script"]}')
    input('Enter чтобы продолжить')
    print()

    while player['hp'] > 0 and enemy_hp > 0:
        if round % 2 == 1:
            print(f'{player["name"]} атакует {enemy["name"]}')
            enemy_hp -= player['attack']
            sleep(1)
            print(f'{player["name"]} -- {player["hp"]}\n{enemy["name"]} -- {enemy_hp}')
            sleep(1)
        else:
            print(f'{enemy["name"]} атакует {player["name"]}')
            player['hp'] -= enemy['attack']
            sleep(1)
            print(f'{player["name"]} -- {player["hp"]}\n{enemy["name"]} -- {enemy_hp}')
            sleep(1)
        round += 1
    if player['hp'] > 0:
        print(f'Противник - {enemy["name"]}: {enemy["win"]}')
    else:
        print(f'Противник - {enemy["name"]}: {enemy["loss"]}')
    player['hp'] = 100


def training():
    training_type = input('''1 - тренировать атаку
2 - тренировать защиту
''') 
    for i in range(0, 101, 20):
        print(f'Тренировка завершена на {i}%')
        sleep(1.5)
    if training_type == '1':
        player['attack'] += 2
        print(f'Тренировка окончена! Теперь ваша величина атаки равна {player["attack"]}')
    elif training_type == '2':
        player['armor'] += 100
        print(f'Тренировка окончена! Теперь ваша величина защиты равна {player["armor"]}')
    print()