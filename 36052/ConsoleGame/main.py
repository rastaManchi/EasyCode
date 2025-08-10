import random
import time


player = {
    'name': '',
    'armor': 0.95,
    'hp': 100,
    'attack': 5,
    'luck': 10,
    'money': 10000,
    'inventory': []
}

enemies = [
    {
        'name': 'Волк', 
        'hp': 10,
        'attack': 10,
        'script': 'Зачем ты здесь? Ты не сможешь меня победить. Принцесса больше не твоя, а чья - не твоя забота. Уходи, пока можешь.',
        'win': 'Ты - достойный противник, но до принцессы тебе всё равно никогда не добраться.',
        'loss': 'Ха! Я же говорил - тебе меня не одолеть. Уходи и не возвращайся.'
    },
    {
        'name': 'Змей Горыныч',
        'hp': 20,
        'attack': 25,
        'script': 'Не ожидал меня встретить? Я, если честно, тоже не думал, что здесь окажусь. После богатырей остаётся только фрилансить, в этот раз сказали защищать долину на пути к замку. В любом случае, ААААААрхрхрархгрх!! Ты не пройдёшь!',
        'win': 'На самом деле, я даже рад, что ты меня победил. Мой босс - дуралей, принцессу не заслужил. Иди дальше. Не зубадь там замолвить за меня словечко. Скажи, что я сражался как лев. Нет.. Как дракон!!',
        'loss': 'Могли бы просто побеседовать. Ты же и сам знал, что у тебя не получится меня убить.. Возвращайся как-нибудь, здесь довольно одиноко.'
    },

    {
        'name': 'Доминик Торетто',
        'hp': 200,
        'attack': 50,
        'script': 'Как ты смог добраться до сюда?! Как ты вообще посмел думать, что можешь со мной сражаться? Ты слаб! Принцесса будет моей, а ты уйдёшь ни с чем. Да будет битва! Самое важное - семья.',
        'win': 'Ты меня убил, но я точно появлюсь в следующей части',
        'loss': 'Прощай..'
    }
]

name = input('Как тебя зовут?: ')
player['name'] = name
current_enemy = 0

while True:
    action = input('''Выбери действие:
1 - В бой!
2 - Тренировка''')
    if action == '1':
        round = random.randint(1, 2)
        enemy = enemies[current_enemy]
        enemy_hp = enemies[current_enemy]['hp']
        print(f'Противник - {enemy["name"]}: {enemy["script"]}')
        input('Enter, чтобы продолжить')
        print()
        while player['hp'] > 0 and enemy_hp > 0:
            if round % 2 == 1:
                print(f'{player["name"]} атакует {enemy["name"]}')
                crit = random.randint(1, 100)
                if crit < player["luck"]:
                    enemy_hp -= player["attack"] * 3
                else:
                    enemy_hp -= player["attack"]
                time.sleep(1)
            else:
                print(f'{enemy["name"]} атакует {player["name"]}')
                player["hp"] -= enemy["attack"] * player['armor']
                time.sleep(1)
            print(f'''{player["name"]} -- {player["hp"]}
{enemy["name"]} -- {enemy_hp}''')
            print()
            time.sleep(1)
            round += 1
        if player["hp"] > 0:
            print(f'Противник - {enemy["name"]}: {enemy["win"]}')
            current_enemy += 1
        else:
            print(f'Противник - {enemy["name"]}: {enemy["loss"]}')
        player["hp"] = 100
    