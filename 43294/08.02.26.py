import turtle

turtle.title('Булат')
turtle.bgcolor('black')

a = turtle.Turtle()
a.speed(1)
# a.hideturtle()
a.color('red')
a.width(10)
a.fillcolor('orange')

b = turtle.Turtle()
b.speed(1)
# b.hideturtle()
b.color('green')
b.width(10)
b.fillcolor('yellow')

a.begin_fill()

a.left(90)
a.forward(100)
a.right(60)
a.forward(80)

a.end_fill()

a.circle(10)

b.begin_fill()
b.backward(100)
b.right(45)
b.forward(140)
b.left(135)
b.forward(100)
b.end_fill()

input()