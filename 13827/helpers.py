from random import randint
from time import sleep
from data import *


def fight(current_enemy):
    round = randint(1, 2)
    enemy = enemies[current_enemy]
    enemy_hp = enemies[current_enemy]['hp']
    print(f'Противник - {enemy["name"]}: {enemy["script"]}')
    input('Enter чтобы продолжить')
    print()
    while player['hp'] > 0 and enemy_hp > 0:
        if round % 2 == 1:
            print(f'{player["name"]} атакует {enemy["name"]}.')
            crit = randint(1, 100)
            if crit < player['luck']:
                print('Критический УРОН!!!')
                enemy_hp -= player['attack'] * 2
            else:
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
        current_enemy += 1
    else:
        print(f'Противник - {enemy["name"]}: {enemy["loss"]}')
    player['hp'] = 100
    print()
    return current_enemy


def training(training_type):
    for i in range(0, 101, 20):
        print(f'Тренировка завершена на {i}%')
        sleep(1.5)
    if training_type == '1':
        player['attack'] += 2
        print(f'Отличная тренировка, теперь величина атаки равна {player["attack"]}')
    elif training_type == '2':
        player['armor'] += 0.15
        print(f'Тренировка завершена, теперь ваша броня поглощает {player["armor"]} урона!')


def shop():
    print('добро пожаловать, путник! Что хочешь приобрести? ')
    print(f'У тебя есть {player["money"]} монет!')
    for key, value in items.items():
        print(f'{key} -- {value["name"]}: {value["price"]}')
    item = input('Выбери предмет: ')
    if items[item]['name'] in player['inventory']:
        print(f'{key} -- {value["name"]}: {value["price"]} | Уже есть')
    elif player['money'] >= items[item]["price"]:
        print('Товар успешно куплен!')
        player['inventory'].append(items[item]['name'])
        player['money'] -= items[item]['price']
    else:
        print('Не хватает денег!')
    print('\nБуду ждать тебя снова, путник\n\n')


def display_inventory():
    print('У вас есть: ')
    for i in player['inventory']:
        print(i)
    print(f'{player["money"]} монет.')
    print()
    if 'Зелье удачи' in player['inventory']:
        potion = input('Жедаешь выпиить зелье удачи? \n1 - Да\n2 - Нет\n')
        if potion == '1':
            player['luck'] += 7
            print(f'Готово! Теперь шанс нанести критический урон возрос!')
            player['inventory'].remove('Зелье удачи')     


def display_player():
    print(f'Игрок - {player["name"]}')
    print(f'Величина атаки - {player["attack"]}')
    print(f'Броня поглощает -- {player["armor"]}')
    print(f'Удача -- {player["luck"]}')
    print()


def display_enemy(current_enemy):
    enemy = enemies[current_enemy]
    print(f'Противник -- {enemy["name"]}')
    print(f'Величина Атаки -- {enemy["attack"]}')
    print(f'Здоровье -- {enemy["hp"]}')
    print()


def earn():
    print('Добро пожаловать на завод! У тебя есть 66.66% шанс заработать 500 монет. Соответственно, 33.33% чтобы их потерять!')
    result = randint(1, 100)
    sleep(1.5)
    print('Результат...')
    sleep(1.5)
    print('Страшно?')
    sleep(1.5)
    pobeda = randint(1, 100)
    if pobeda < player['luck']:
        print('Критическая удача!!!\nВы выиграли 5000000 монет!')
        player['money'] += 5000000
    else:
        if result < 67:
            print('Вы выиграли 500 монет!')
            player['money'] += 500
        else:
            print('Вы проиграли 500 монет!')
            player['money'] -= 500
    print()
    print(f'Осталось монет: {player["money"]}')
    print()
