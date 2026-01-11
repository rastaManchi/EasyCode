# w - write
# a - add
# r - read


# file = open('save.txt', 'r', encoding='utf-8')
# # file.write('Булат cheater\n')
# data = file.read()
# file.close()
# accounts = data.split('\n')
# account_data = accounts[0].split(' - ')
# print(account_data[1])


file1 = open("text1.txt", "r", encoding="utf-8")
file2 = open("text2.txt", "a", encoding="utf-8")
a = (file1.read()).split("\n")
b = len(a)
c = 0
for i in range(b):
    c -= 1
    file2.write(a[c])
    file2.write("\n")

file2.close()


