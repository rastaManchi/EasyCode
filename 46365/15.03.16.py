import math


g = float(input())
R = float(input())
h = float(input())

u = math.sqrt(g*math.pow(R, 2)/(R + h))
print(u)


# scores = []
# for i in range(10):
#     num = int(input())
#     scores.append(num)
# print(max(scores))