import tkinter as tk


current_shape = "line"
start_x = None
start_y = None


def set_shape(shape):
    global current_shape
    current_shape = shape


def on_button_press(event):
    global start_x, start_y
    start_x = event.x
    start_y = event.y


def on_mouse_drag(event):
    canvas.delete("temp")
    if current_shape == "line":
        canvas.create_line(start_x, start_y, event.x, event.y, tags="temp")
    elif current_shape == "rect":
        canvas.create_rectangle(start_x, start_y, event.x, event.y, tags="temp")
    elif current_shape == "circle":
        canvas.create_oval(start_x, start_y, event.x, event.y, tags="temp")


def on_button_release(event):
    if current_shape == "line":
        canvas.create_line(start_x, start_y, event.x, event.y)
    elif current_shape == "rect":
        canvas.create_rectangle(start_x, start_y, event.x, event.y)
    elif current_shape == "circle":
        canvas.create_oval(start_x, start_y, event.x, event.y)


def clear_canvas():
    canvas.delete("all")


root = tk.Tk()
root.title("рисовашка")

canvas = tk.Canvas(root, bg="white", width=400, height=400)
canvas.pack()
canvas.bind("<Button-1>", on_button_press)
canvas.bind("<B1-Motion>", on_mouse_drag)
canvas.bind("<ButtonRelease-1>", on_button_release)

button_frame = tk.Frame(root)
button_frame.pack()

line_btn = tk.Button(button_frame, text="Линия", command=lambda: set_shape("line"))
line_btn.pack(side=tk.LEFT)

rect_btn = tk.Button(button_frame, text="Прямоугольник", command=lambda: set_shape("rect"))
rect_btn.pack(side=tk.LEFT)

circle_btn = tk.Button(button_frame, text="Круг", command=lambda: set_shape("circle"))
circle_btn.pack(side=tk.LEFT)

clear_btn = tk.Button(button_frame, text="Очистить", command=clear_canvas)
clear_btn.pack(side=tk.LEFT)


root.mainloop()