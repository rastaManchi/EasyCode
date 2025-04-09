names = ['Максим', 'Булат', 1, 2, 3, False, True, []]
names[1] = 'Булат Закиров'


# names.append(2025) Добавление в конец списка
# names.insert(0, 2025) Добавление в конкретный индекс списка, например 0


# names.pop(0) Удаление элемента по индексу, если в скобках ничего нет, то удаляется последний элемент
# del names[1] Удаение по индексу
# names.remove(1) Удаление по значению

# for i in range(0, len(names)):
#     print(names[i])

# index_count = 0
# for i in names:
#     print(i)
#     index_count += 1

user = {
    'login': '123',
    'pass': 'qwerty'
}

user['login'] = '123'
user['new'] = 'Булат'
del user['login']


users = [
    {
        'login': '123',
        'password': 'qwerty',
        'inventory': [
            {
                'name': 'sword',
                'damage': 120
            }
        ]
    },
    {
        'login': '456',
        'pass': 'qwerty123'
    }
]
print(users[0]['inventory'][0]['damage'])