from random import randint
from time import sleep

from data import *


def fight(ce):
    round = randint(1, 2)
    enemy = enemies[ce]
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
            else:
                enemy_hp -= player['attack']
            sleep(1)
            print(f'''{player["name"]} -- {player["hp"]}
    {enemy["name"]} -- {enemy_hp}''')
            print()
            sleep(1)
        else:
            print(f'{enemy["name"]} атакует {player["name"]}')
            player['hp'] -= enemy['attack'] * player['armor']
            sleep(1)
            print(f'''{player["name"]} -- {player["hp"]}
    {enemy["name"]} -- {enemy_hp}''')
            print()
            sleep(1)
        round += 1
    if player['hp'] > 0:
        player['hp'] = 100
        print(f'Противник -- {enemy["name"]}: {enemy["win"]}')
        return ce + 1
    else:
        player['hp'] = 100
        print(f'Противник -- {enemy["name"]}: {enemy["loss"]}')
        return ce


def training():
    skip = '2'
    if shop_items['2']['name'] in player['inventory']:
        skip = input('Желаете пропустить тренировку?\n1 - Да\n2 - Нет\n')
    training_type = input('Какой вид тренировки:\n1 - Урон\n2 - Защита\n')
    if skip == '2':
        for i in range(0, 101, 20):
            print(f'Тренировка завершена на {i}%')
            sleep(1.5)
    if training_type == '1':
        player['attack'] += 2
        print(f'Тренировка окончена! Теперь ваша величина атаки равна {player["attack"]}')
    elif training_type == '2':
        player['armor'] -= .09
        print(f'Тренировка окончена! Теперь броня поглощает {100 - player["armor"] * 100}% урона')
    print()


def display_player():
    print(f'Игрок - {player["name"]}')
    print(f'Величина атаки - {player["attack"]}. Шанс критического урона ({player["attack"] * 3}ед.) равен {player["luck"]}%')
    print(f'Броня поглощает {(1 - player["armor"]) * 100}% урона')
    print()


def display_enemy(ce):
    enemy = enemies[ce]
    print(f'Противник - {enemy["name"]}')
    print(f'Величина атаки - {enemy["attack"]}')
    print(f'Здоровье - {enemy["hp"]}')
    print()



def shop():
    print('Добро пожаловать, путник! Что хочешь приобрести?')
    print(f'У тебя есть {player["money"]} монет.')
    for key, value in shop_items.items():
        print(f'{key} - {value["name"]}: {value["price"]}')

    item = input()
    if shop_items[item]['name'] in player['inventory']:
        print(f'У тебя уже есть {shop_items[item]["name"]}')
    elif player['money'] >= shop_items[item]['price']:
        print(f'Ты успешно приобрёл {shop_items[item]["name"]}')
        player['inventory'].append(shop_items[item]["name"])
        player['money'] -= shop_items[item]['price']
    else:
        print('Не хватает монет :(')
    print()
    print('Буду ждать тебя снова, путник!')
    print()


def earn():
    print('Добро пожаловать на завод! У тебя есть 66.66% шанс заработать 500 монет. Соответственно, 33.33% чтобы их потерять')
    result = randint(1, 100)
    sleep(1.5)
    print('Результат....')
    sleep(1.5)
    print('Страшно?!')
    if result < 67:
        print('Вы выиграли 500 монет!')
        player['money'] += 500
    else:
        print('Вы проиграли 500 монет :(')
        player['money'] -= 500
    print()
    print(f'Осталось монет: {player["money"]}')
    print()


def display_inventory():
    print(f'У вас есть:')
    for value in player['inventory']:
        print(value)
    print(f'{player["money"]} монет.')
    print()
    if 'Зелье удачи' in player['inventory']:
        potion = input('''Желаешь выпить зелье удачи?
    1 - да
    2 - нет
    ''')
        if potion == '1':
            player['luck'] += 7
            print(f'Готово! Теперь шанс нанести критический урон равен {player["luck"]}%')
            player['inventory'].remove('Зелье удачи')