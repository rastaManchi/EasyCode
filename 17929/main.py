from random import randint
from time import sleep

from data import *
from functions import *


name = input('Введи свое имя, путник: ')
player['name'] = name
current_enemy = 0

while True:
    action = input('Выбери действие:\n1-В бой\n2-Тренировка\n')
    if action == '1':
        fight(current_enemy)
    elif action == '2':
        training()

