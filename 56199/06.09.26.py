import tkinter as tk


root = tk.Tk()
root.title("рисовашка")

canvas = tk.Canvas(root, bg="white", width=800, height=800)
canvas.pack()

button_frame = tk.Frame(root)
button_frame.pack()

line_btn = tk.Button(button_frame, text="Линия")
line_btn.pack(side=tk.LEFT)

rect_btn = tk.Button(button_frame, text="Прямоугольник")
rect_btn.pack(side=tk.LEFT)

circle_btn = tk.Button(button_frame, text="Круг")
circle_btn.pack(side=tk.LEFT)

clear_btn = tk.Button(button_frame, text="Очистить")
clear_btn.pack(side=tk.LEFT)


root.mainloop()