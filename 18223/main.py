spisok = ['Молоко', 'Яблоки', 'Сок', 'Вода']

spisok.append("Туалетную бумагу")

spisok.pop(1)
spisok.remove("Сок")
del spisok[0]
print(spisok)

for i in spisok:
    print(i)


print(len(spisok))

# films = []

# for i in range(3):
#     film_name = input('Введите название фильма: ')
#     films.append(film_name)

# print(films)

# delete_name = input('Введите последний просмотренный фильм: ')
# if delete_name in films:
#     print('Фильм удален из списка')
#     films.remove(delete_name)
# else:
#     print('Такого фильма в списе нет!')

# print( films)