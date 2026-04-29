import turtle


turtle.title("Window")
turtle.bgcolor('gray')


a = turtle.Turtle()
a.color('white')


num = int(input('Кол-во концов: '))
angle = 180 - abs(180 - (180*(num-2)/(num/2)))
for i in range(num):
    a.forward(100)
    a.right(angle)
    
input()