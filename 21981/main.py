items = {
    'Яблоко': 80,
    'ПК': 50000,
    'ручка': 50
}

items['ПК']
items['ПК'] = 70000 # изменение значения
items['new_key'] = 'new_value' # добавление новой пары
del items['ручка'] # удаление элемента

keys = list(items.keys()) # список только ключей
values = list(items.values()) # список только значений
items_ = list(items.items()) # список элементов

# for key, value in items_:
#     print(key, value)

# spisok = [1, 2, 'Булат', 4, 5]
# for i in spisok:
#     print(i)


# for i in items:
#     print(i)
#     print(items[i])