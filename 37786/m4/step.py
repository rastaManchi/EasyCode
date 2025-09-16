import random
import time
from data import *
from helpers import *


name = input('Введите свое имя, путник: ')
player["name"] = name

current_enemy = 0
enemy = enemies[current_enemy]
enemy_hp = enemy['hp']


while True:
    command = input('''1 - В бой
2 - Тренировка
3 - Магазин
''')
    if command == '1':
        current_enemy = fight(current_enemy)
    elif command == '2':
        training()
    elif command == '3':
        shop()

