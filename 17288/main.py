min_x = -5
max_x = 5
min_y = -5
max_y = 5

for y in range(min_y, max_y+1):
    for x in range(min_x, max_x+1):
        print('*', end=' ')
    print()



all_damage = 0 
hp = 100

for i in range(5):
    hp -= 5
    all_damage += 5

print('Здоровье', hp)
print('Полученный урон', all_damage)