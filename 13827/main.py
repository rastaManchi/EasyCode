
names = ["Булат", 'Илья', 'Марк']
print(f"В компании: {names}")
names[0] = "Михаил"
print(f"Булат уволился, пришел Михаил: {names}")
names.append("Павел") #добавить элемент в список 
print(f"Добавили Павла: {names}")
names.append("Валера")
print(f"Добавили Валеру: {names}")

# Удаление по индексу
names.pop(0)

# Удаление по значению
names.remove("Павел")
print(names)

if "Валера" in names: # проверка наличия элемента в списке
    names.remove("Валера")
    print(f'Валера Нашелся, мы его уволили\n{names}')
    
else:
    print('Валера не найден!')

print(f"В комании осталось {len(names)} человек\n{names}")