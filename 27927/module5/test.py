import json


dictionary = {
    "Ключ1": 'Значение1',
    "Ключ2": 'Значение2',
    "Ключ3": 'Значение3'
}


print(dictionary)
print('_'*100)
json_object = json.dumps(dictionary)
print(json_object)