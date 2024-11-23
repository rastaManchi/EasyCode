names = ['Булат', 'Артем', 'Герман', 'Анна', 1231231, False] 

print(names[0:4])
names[4] = 'Максим'
names[5] = 'Андрей'

# Добавление
names.append("Петр")
names.insert(0, 'Алиса')

# Удаление
names.pop(0)
del names[-1]
# names.remove("Петр")

if 'Петр' in names:
    print('Петр найден!')

count = len(names)

print(names)
for i in range(count):
    print(names[i])


for name in names:
    print(name)





print('''
Привет
Меня зовут Булат
''')