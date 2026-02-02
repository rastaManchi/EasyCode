# dict_ = {
#     'ключ': 'значение',
#     'ключ2': 'значение2'
# }

# dict_['Новый'] = 100
# print(dict_['Новый'])

# dict_['Новый'] = 150
# print(dict_.get('Новый'))

# del dict_['Новый']


# print(dict_.values())
# print(dict_.keys())
# dict_.clear()
# print(dict_)



dict_ = {}
command = input()
while command != '-1':
    if command == '1':
        name = input()
        summa = input()
        dict_[name] = summa
    elif command == '2':
        name = input()
        if name in dict_:
            summa = input()
            dict_[name] += summa
    elif command == '4':
        name = input()
        if name in dict_:
            summa = input()
            dict_[name] -= summa