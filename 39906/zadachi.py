import turtle

t = turtle.Turtle()
a = int(input("Введите количество лучей: "))
b = 0
while b <= a:
    b += 1
    t.forward(200)
    t.right(180-180/a)



input()