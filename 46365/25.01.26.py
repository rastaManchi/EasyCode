dict_ = {
    'ключ': 'значение',
    'ключ2': 'значение2'
}

dict_['Новый'] = 100
print(dict_['Новый'])

dict_['Новый'] = 150
print(dict_.get('Новый'))

del dict_['Новый']


print(dict_.values())
print(dict_.keys())
dict_.clear()
print(dict_)