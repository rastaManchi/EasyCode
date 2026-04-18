import random
import string
symbols = list(string.ascii_lowercase)
text = input('Введите текст: ')
new_text = ''
for symbol in text:
    if symbol == ' ':
        new_text += symbol
    else:
        new_text += random.choice(symbols)
print(new_text)

