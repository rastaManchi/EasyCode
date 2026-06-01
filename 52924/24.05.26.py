# dict_ = {
#     1: 'один',
#     2: 'два'
# }

# print(dict_.values())
# print(dict_.keys())
# print(dict_.items())

# for key, value in dict_.items():
#     print(f"Ключ: {key} -- Значение: {value}")


countries = {}

while True:
    command = input('1-Добавить 2-Узнать столицу')
    if command == '1':
        country = input('Введите название страны: ')
        city = input('Введите столицу: ')
        countries[country] = city
    elif command == '2':
        country = input('Введите название страны: ')
        print(f'Столица: {countries.get(country, "Этой страны в базе нет")}')