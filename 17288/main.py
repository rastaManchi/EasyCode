character = ['Тревор', 50, 50, 100, 'джип']


character_dict = {
    'name': 'Тревор',
    'age': 50,
    'damage': 50,
    'hp': 100,
    'car': 'Джип'
}

character_dict['damage'] = 100

character_dict['new_key'] = 'Новое значение'

del character_dict['car']

if 'car' in character_dict:
    del character_dict['car']


print(list(character_dict.items()))
[
 ('name', 'Тревор'), 
 ('age', 50), 
 ('damage', 100),
 ('hp', 100), 
 ('new_key', 'Новое значение')
 ]

for i in character_dict:
    print(f'{i} -- {character_dict[i]}')

for key, value in character_dict.items():
    print(f'{key} -- {value}')



character_dict.keys()
character_dict.values()

