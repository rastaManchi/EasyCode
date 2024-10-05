import random


min_x = -5
max_x = 5
min_y = -5
max_y = 5

for y in range(min_y, max_y+1):
    for x in range(min_x, max_x+1):
        print('*', end=' ')
    print()


fire_coords = []

for i in range(10):
    fire_coords.append({'x': random.randint(-5,5),
                        'y': random.randint(-5,5)})

print(fire_coords)