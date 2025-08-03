import random

# камень - 1
# ножницы - 2
# бумага - 3

user_choice = int(input('Выбери: \n1-камень\n2-ножницы\n3-бумага\n'))
pc_choice = random.randint(1, 3)

if user_choice == 1:
    if pc_choice == 1:
        print('Ничья')
    elif pc_choice == 2:
        print('Вы победили')
    elif pc_choice == 3:
        print('Вы проиграли')
if user_choice == 2:
    if pc_choice == 1:
        print('Вы проиграли')
    elif pc_choice == 2:
        print('Ничья')
    elif pc_choice == 3:
        print('Вы победили')
if user_choice == 3:
    if pc_choice == 1:
        print('Вы победили')
    elif pc_choice == 2:
        print('Вы проииграли')
    elif pc_choice == 3:
        print('Ничья')
        