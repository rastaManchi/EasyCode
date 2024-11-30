products_dict = {
    'Кастрюля': 500,
    'Тарелка': 300
}

# print(products_dict['Кастрюля'])

# products_dict['Тарелка'] = 600
# products_dict['NEW'] = 3000

# del products_dict['NEW']

for key, value in products_dict.items():
    print(f'Ключ: {key} -- Значение: {value}')

products_dict.items()
products_dict.keys()
products_dict.values()
