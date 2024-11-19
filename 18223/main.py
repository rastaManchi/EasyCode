import random

user_choice = int(input('Выбери:\n1-ножницы\n2-камень\n3-бумага\n'))
pc_choice = random.randint(1, 3)

if (user_choice == 1 and pc_choice == 3) or \
    (user_choice == 2 and pc_choice == 1) or \
    (user_choice == 3 and pc_choice == 2):
    print('Вы победили')
elif user_choice == pc_choice:
    print('Ничья')
else:
    print('Вы проиграли!')
print(f'Пользователь {user_choice} -- Компьютер {pc_choice}')
