file = open('23963/test.txt', 'r', encoding='UTF-8')
text = file.readlines()
print(text[-1])
file.close()

with open('23963/test.txt', 'r') as file:
    text = file.readlines()
    print(text[-1])
    file.close()


a = 5
b = 10
with a+b as c:
    print(c)
