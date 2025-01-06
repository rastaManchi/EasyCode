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
            crit = randint(1, 100)
            if crit < player['luck']:
                enemy_hp -= player['attack'] * 3
                print('Критический урон!')
            else:
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


def display_player():
    print(f'Игрок -- {player["name"]}')
    print(f'Величина атаки - {player["attack"]}. Шанс критического урона ({player["attack"] * 3}ед.) равен {player["luck"]}%')
    print(f'Броня поглощает {player["armor"]}ед. урона')
    print()


def display_enemy(current_enemy):
    enemy = enemies[current_enemy]
    print(f'Противник - {enemy["name"]}')
    print(f'Величина атаки - {enemy["attack"]}')
    print(f'Здоровье - {enemy["hp"]}')
    print()


def display_inventory():
    print(f'У вас есть:')
    for value in player['inventory']:
        print(value)
    print(f'{player["money"]} монет.')
    if 'Зелье удачи' in player['inventory']:
        potion = input('Желаешь ли ты выпить зелье удачи? \n1 - Да\n2 - нет\n')
        if potion == '1':
            player['luck'] += 7
            print(f'Готово! Теперь шанс нанести критический урон равен {player["luck"]}%')
            player['inventory'].remove('Зелье удачи')


def shop():
    print('Добро пожаловать, путник! Что хочешь приобрести?')
    print(f'У тебя есть {player["money"]} монет.')
    for key, value in items.items():
        print(f'{key} - {value["name"]}: {value["price"]}')
    
    item = input()
    if item in player['inventory']:
        print(f'У тебя уже есть {items[item]["name"]}')
    elif player['money'] >= items[item]['price']:
        print(f'Ты успешно приобрел {items[item]["name"]}')
        player['invntory'].append(items[item]["name"])
        player['money'] -= items[item]['price']
    else:
        print('Не хватает монет :(')
    print()
    print('Буду ждать тебя снова, путник!')
    print()


def earn():
    print('Добро пожаловать на завод! У тебя есть 66.66% шанс заработать 500 монет! Соответственно, 33.33% чтобы их потерять')
    result = randint(1, 100)
    sleep(1.5)
    print('Результат...')
    sleep(1.5)
    print('Страшно?')
    if result < 67:
        print('Вы выиграли 500 монет!')
        player['money'] += 500
    else:
        print('Вы проиграли в "21" 500 монет(')
        player['money'] -= 500
    print()
    print(f'Осталось монет: {player["money"]}')
    print()