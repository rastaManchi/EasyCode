names = []
feeds = []
animals = []


for i in range(10):
    name = input()
    feed = 0
    animal = input()
    names.append(name)
    feeds.append(feed)
    animals.append(animal)


action = input('Что вы хотите сделать 1-покормить/2-информация о животных: ')
while action != 'stop':
    if action == '1':
        animal_name = input('Введите имя животного: ')
        for i in range(10):
            if names[i] == animal_name:
                if feeds[i] < 3:
                    feeds[i] += 1
                    print('Покормили')
                else:
                    print('Животное сыто')
    elif action == '2':
        for i in range(10):
            print(f"{animals[i]} {names[i]} Сегодня кушал {feeds[i]} раз")
    
    action = input('ЧТо вы хотите сделать 1-покормить/2-информация о животных: ')        
