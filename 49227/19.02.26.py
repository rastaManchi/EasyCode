# a = "login - password -- login2 - password2"
# print(a.split(' -- '))

# spisok_ = ['Булат', 'Роберт', 'Илья']

# result = ', '.join(spisok_)
# print(result)


cookbook = {
    'Яичница': ['2 яйца', 'чайная ложка соли'],
    'Яичница с сосисками':  ['2 яйца', 'чайная ложка соли', 'Сосиски']
}

search = input()
# print(f"{search}: {cookbook[search]}")
ing = [{name: cookbook[name]} for name in cookbook if search in name]
print(ing)