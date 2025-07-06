names = ['Иван', 'Роберт', 'Артем', 'Катя', 'Максим', 'Женя']
# names.append('12') Добавить
# names.remove('12') Удалить по значению
# names.pop(1) Удалить по индексу
# names[0] Элемент с индексом ноль
# if '12' in names: проверка элеменита в списке
# if 3 < len(names) проверка индекса в списке
# film1 = input('введите название фильма')
films = []

for i in range(3):
    film_name = input('Введите название фильма: ')
    films.append(film_name)
    
print(films)