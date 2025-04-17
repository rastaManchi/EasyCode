import time

spisok1 = ['Привет, ', 'Привет, ', 'Привет, ']

print(spisok1)
print('_'*100)

count = 0
for enemy in spisok1:
    spisok1[count] += 'чье-то имя'
    print(spisok1)
    print('_'*100)
    time.sleep(15)
    count+=1

print('Все')