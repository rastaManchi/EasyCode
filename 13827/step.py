from data import *
from helpers import *
from random import randint
from time import sleep


name = input('Введи своё имя, путник: ')
player['name'] = name
current_enemy = 0


while True:
    action = input('Выберите днйствие:\n \
                   1 - В бой!\n \
                   2 - Тренировка\n \
                   3 - Магазин\n \
                   4 - Завод\n \
                   5 - Показать инвентарь\n \
                   6 - Информация об игроке\n \
                   7 - информация о текущем противнике\n')
    if action == '1':
        current_enemy = fight(current_enemy)
    elif action == '2':
        training_type = input('Выберите тип тренировки:\n1 - тренировать атаку\n2 - тренировать оборону\n')
        training(training_type)
    elif action == '3':
        shop()
    elif action == '4':
        earn()
    elif action == '5':
        display_inventory()
    elif action == '6':
        display_player()
    elif action == '7':
        display_enemy(current_enemy)