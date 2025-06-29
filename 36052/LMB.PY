import random


# 1 - Камень
# 2 - Ножницы
# 3 - Бумажка

choices = {
    1: 'Камень',
    2: 'Ножницы',
    3: 'Бумага'
}

user_choice = int(input('Выбери:\n1-Камень\n2-Ножницы\n3-Бумажка'))
pc_choice = random.randint(1, 3)
if user_choice == 1:
    if pc_choice == 1:
        print(f'PC - {choices[pc_choice]}\nPlayer - {choices[user_choice]}\n')
        print('Ничья')
    elif pc_choice == 2:
        print(f'PC - {choices[pc_choice]}\nPlayer - {choices[user_choice]}\n')
        print('Ты победил')
    else:
        print(f'PC - {choices[pc_choice]}\nPlayer - {choices[user_choice]}\n')
        print('ПК победил')
elif user_choice == 2:
    if pc_choice == 1:
        print(f'PC - {choices[pc_choice]}\nPlayer - {choices[user_choice]}\n')
        print('ПК победил')
    elif pc_choice == 2:
        print(f'PC - {choices[pc_choice]}\nPlayer - {choices[user_choice]}\n')
        print('Ничья')
    else:
        print(f'PC - {choices[pc_choice]}\nPlayer - {choices[user_choice]}\n')
        print('Ты победил')