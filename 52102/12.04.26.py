import tkinter as tk 
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Омэрэканский бургэр")
root.geometry('500x500')


canvas = tk.Canvas(background="#334649",
                    width=250,
                    height=250)
canvas.pack()


canvas.create_line(
    0,
    250//3,
    250,
    250//3
)

canvas.create_line(
    0,
    250//3 * 2,
    250,
    250//3 * 2
)

canvas.create_line(
    250//3,
    0,
    250//3,
    250
)

canvas.create_line(
    250//3 * 2,
    0,
    250//3 * 2,
    250
)


root.mainloop()