import turtle

turtle.title("Название окна")
turtle.bgcolor("black")
turtle.speed(0.1)

cursor = turtle.Turtle()
cursor.width(10)
cursor.color('white')
cursor.up()
cursor.forward(300)
cursor.down()
cursor.right(90)
cursor.backward(200)

cursor.begin_fill()

cursor.right(45)
cursor.forward(50)
cursor.right(45)
cursor.forward(50)

cursor.end_fill()


input()