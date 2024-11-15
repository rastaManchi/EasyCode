from data import *
from helpers import *
from random import randint
from time import sleep


name = input('Введи своё имя, путник: ')
player['name'] = name
current_enemy = 0


while True:
    action = input('Выберите днйствие:\n1 - В бой!\n2 - Тренировка\n')
    if action == '1':
        fight(current_enemy)
    elif action == '2':
        training_type = input('Выберите тип тренировки:\n1 - тренировать атаку\n2 - тренировать оборону\n')
        training(training_type)