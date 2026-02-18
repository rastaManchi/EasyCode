import turtle

t = turtle.Turtle()
t.speed(-1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
t.penup()

size = 50

for i in range(8):
    for j in range(8):
        x = j * size
        y = i * size
        t.goto(x, y)
        if (i + j) % 2 == 0:
            t.fillcolor("white")
        else:
            t.fillcolor("black")
        t.begin_fill()
        for _ in range(4):
            t.forward(size)
            t.right(90)
        t.end_fill()

t.penup()
t.goto(0, -50)
t.pendown()
t.pencolor("black")
t.pensize(3)
for _ in range(4):
    t.forward(8 * size)
    t.left(90)

t.hideturtle()
turtle.done()