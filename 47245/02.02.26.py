import tkinter as tk
from tkinter.messagebox import *


current_shape = "line"
start_x = None
start_y = None
canvas = None


def set_shape(shape):
    global current_shape
    current_shape = shape
    
def clear_canvas():
    canvas.delete("all")  


def on_button_press(event):
    global start_x, start_y
    start_x = event.x
    start_y = event.y
    

def on_mouse_drag(event):
    global start_x, start_y
    canvas.delete("temp")
    if current_shape == "line":
        canvas.create_line(start_x, start_y, event.x, event.y, tags="temp")
    elif current_shape == "rectangle":
        canvas.create_rectangle(start_x, start_y, event.x, event.y, tags="temp")
    elif current_shape == "circle":
        r = ((event.x - start_x) ** 2 + (event.y - start_y) ** 2) ** 0.5
        canvas.create_oval(start_x - r, start_y - r, start_x + r, start_y + r, tags="temp")

    

def on_button_release(event):
    global start_x, start_y
    if current_shape == "line":
        canvas.create_line(start_x, start_y, event.x, event.y)
    elif current_shape == "rectangle":
        canvas.create_rectangle(start_x, start_y, event.x, event.y)
    elif current_shape == "circle":
        r = ((event.x - start_x) ** 2 + (event.y - start_y) ** 2) ** 0.5
        canvas.create_oval(start_x - r, start_y - r, start_x + r, start_y + r)



root = tk.Tk()
root.title("Рисовашка")

canvas = tk.Canvas(root, bg="blue", width=800, height=600)
canvas.pack()

button_frame = tk.Frame(root)
button_frame.pack()
line_button = tk.Button(button_frame, text="Линия", command=lambda: set_shape("line"))
line_button.pack(side=tk.LEFT)
rect_button = tk.Button(button_frame, text="Прямоугольник", command=lambda: set_shape("rectangle"))
rect_button.pack(side=tk.LEFT)
circle_button = tk.Button(button_frame, text="Круг", command=lambda: set_shape("circle"))
circle_button.pack(side=tk.LEFT)
clear_button = tk.Button(button_frame, text="Очистить", command=clear_canvas)
clear_button.pack(side=tk.LEFT)


canvas.bind("<Button-1>", on_button_press)
canvas.bind("<B1-Motion>", on_mouse_drag)
canvas.bind("<ButtonRelease-1>", on_button_release)


root.mainloop()

