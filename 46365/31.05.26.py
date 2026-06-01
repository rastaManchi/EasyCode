import re


text = """Номер: +7(999)999-99-90
Номер: +7(999)999-99-99
Номер: 1234678990
123-456
"""
pattern = r"Номер: \+[0-9]?\([0-9]*\)[0-9]*-[0-9]*-[0-9]*"

# result = re.findall(pattern, text)

# match = re.search(pattern, text)
# result = match.group()

# result = re.sub(pattern, "Обработано", text)

# result = re.split(r"\d", text)

# Я родился 29 декабря 2001
29, 2001
2030
6

start_text = input('Введите текст, с которого будет начинаться предложение: ')
pattern = r"^" + start_text

check_text = input('Введите текст: ')
result = re.match(pattern, check_text)
if result:
    print('Бот обработает')
else:
    print('Бот не обработает')