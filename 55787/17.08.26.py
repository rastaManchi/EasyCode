# Вложенные конструкции (структуры данных)

# characters = [
#     {
#         'name': 'Булат',
#         'surname': 'Закиров',
#         'age': 24,
#         'hp': 100
#     },
#     {
#         'name': 'Иван',
#         'surname': 'Иванов',
#         'age': 30,
#         'hp': 75
#     },
#     {
#         'name': 'Илан',
#         'surname': 'Михайлович',
#         'age': 2400,
#         'hp': 2400
#     }
# ]

# print(characters[2]['hp'])

cars = {
    'BMW': {
        'X5': {
            'power': 700,
            'price': 3500000,
            'year': 2017
        },
        'i8': {
            'power': 700,
            'price': 3500000,
            'year': 2014
        }
    }
}

print(cars['BMW']['i8'])


a = [
    [
        {}
    ]
]