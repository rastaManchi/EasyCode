dict_ = {"ключ1": 'значение1', 'ключ2': 'значение2'}

# for i in dict_:
#     print(i, dict_[i])

# print(list(dict_.keys()))
# print(list(dict_.values()))
# print(list(dict_.items()))

for i in dict_.items():
    key, value = i
    print(key, value)
