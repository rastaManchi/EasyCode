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


root = tk.Tk()
root.title("рисовашка")

canvas = tk.Canvas(root, bg="white", width=800, height=800)
canvas.pack()
canvas.bind("<Button-1>", on_button_press)

button_frame = tk.Frame(root)
button_frame.pack()

line_btn = tk.Button(button_frame, text="Линия", command=lambda: set_shape("line"))
line_btn.pack(side=tk.LEFT)

rect_btn = tk.Button(button_frame, text="Прямоугольник", command=lambda: set_shape("rect"))
rect_btn.pack(side=tk.LEFT)

circle_btn = tk.Button(button_frame, text="Круг", command=lambda: set_shape("circle"))
circle_btn.pack(side=tk.LEFT)

clear_btn = tk.Button(button_frame, text="Очистить")
clear_btn.pack(side=tk.LEFT)


root.mainloop()