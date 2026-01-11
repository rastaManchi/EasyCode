while True:
    age = int(input('Сколько вам лет? '))
    if age == -1:
        break
    elif age < 18:
        continue
    name = input('Как вас зовут: ')
    