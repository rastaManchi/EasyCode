# Напишите программу, которая запишет в список все числа от 1 до n
# На вход программе подается число n

# numbers = []
# n = int(input('Введите число: ')) # "10" -> int("10") -> 10

# for i in range(1, n+1):
#     numbers.append(i)
    
# print(numbers)


# url = 'https://vk.com/username=bulat'
# # # url = 'I love EasyCode'
# print(url.split('/'))


# text = ['https:', '', 'vk.com', 'username=bulat']
# joined = "/".join(text)
# print(joined)


number = int(input('Введите число: '))
for i in range(2, number+1, 2):
    print(i)