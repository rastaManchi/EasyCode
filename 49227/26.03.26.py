import math


n = int(input())
print(math.pi)
drob = str(float(math.pi)).split('.')[1]
print(drob[n-1])
