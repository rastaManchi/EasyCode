import os


if not os.path.exists('new.txt'):
    open('new.txt', 'w').close()
else:
    print('Файл найден')


# file = open('file.txt', 'r', encoding='UTF-8')
# result = file.readlines()
# print(result)
# file.close()


# file = open('file.txt', 'a', encoding='UTF-8')
# file.write('Hello world!!!\n')


# with open('file.txt', 'r', encoding='UTF-8') as file:
#     result = file.readlines()
#     print(result)