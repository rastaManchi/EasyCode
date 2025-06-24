word = input('Введите слово:')
# index = len(word) - 1
# print(f'Первая буква: {word[0]}\nПоследняя буква: {word[index]}')
print(f'Первая буква: {word[0]}\nПоследняя буква: {word[-1]}')

print(f'{word[-1:0:-1]}{word[0]}')