films = {
   'Магия': [
        ['Гарри Поттер и Философский Камень', 2001],
        ['Фантастические твари и где они обитают', 2016],
        ['Хроники Нарнии', 2005]
    ],
   'Фантастика': [
        ['Матрица', 1999],
        ['Господин Никто', 2000],
        ['Я - начало', 2014]
    ],
   'Космос': [
       ['Интерстеллар', 2014],
       ['Марсианин', 2015],
       ['Пассажиры', 2016]
   ],
   'Marvel': [
       ['Мстители: Война бесконечности', 2018],
       ['Дэдпул', 2016],
       ['Стражи галактики', 2014]
   ]
}


for film_key in films:
    all_films = films[film_key]
    for film in all_films:
        film_name = film[0]
        film_age = film[1]
        print(f'{film_name} -- {film_age}')

print('_'*100)
# films['Магия'].append(['Ученик Чародея', 2010])
# films['Фантастика'].append(['Лекарство от здоровья', 2017])
# films['Космос'].append(['Время первы[]', 2017])
# films['Marvel'].append(['Веном 2', 2021])

for film_key in films:
    all_films = films[film_key]
    if film_key == 'Магия':
        all_films.append(['msdlsnfdsf', 10212])

for film_key in films:
    all_films = films[film_key]
    print(film_key)
    print()
    for film in all_films:
        film_name = film[0]
        film_age = film[1]
        print(f'{film_name} -- {film_age}')
    print('\n')
    print('_' * 30)

