from random import randint
from time import sleep


from data import *
from helpers import *


name = input('Введи свое имя, путник: ')
player['name'] = name
current_enemy = 0


while True:
    action = input('''Выбери действие:
1 - В бой!
2 - Тренировка''')
    if action == '1':
        fight(current_enemy)
    elif action == '2':
        training()