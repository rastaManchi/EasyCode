file = open('test.txt', 'r', encoding="UTF-8")
text = file.readlines()
print(text)

# print(open('test.txt', 'r').read())

file = open('test.txt', 'w', encoding='UTF-8')
# file = open('test.txt', 'a', encoding='UTF-8')
file.write('Пока мир')
file.close()