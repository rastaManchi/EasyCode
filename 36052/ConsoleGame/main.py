import random
import time
from data import *
from functions import *


name = input('Как тебя зовут?: ')
player['name'] = name
current_enemy = 0


while True:
    action = input('''Выбери действие:
1 - В бой!
2 - Тренировка
3 - Новая команда''')
    if action == '1':
        current_enemy = fight(current_enemy)
    elif action == '2':
        training()
    