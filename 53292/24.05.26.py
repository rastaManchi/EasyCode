import tkinter as tk
from PIL import Image, ImageTk


root = tk.Tk()

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400

canvas = tk.Canvas(
    background='gray',
    width=CANVAS_WIDTH,
    height=CANVAS_HEIGHT
)
canvas.pack()

size_x = CANVAS_WIDTH // 8
size_y = CANVAS_HEIGHT // 8

offset_x, offset_y = 0, 0
count_row = 1
count_column = 1
for column in range(8):
    offset_x = 0
    count_column=1
    for row in range(8):
        if (count_row + count_column) % 2 == 0:
            canvas.create_rectangle(
                offset_x, offset_y,
                offset_x+size_x, offset_y+size_y,
                fill='black'
            )
        else:
            canvas.create_rectangle(
                offset_x, offset_y,
                offset_x+size_x, offset_y+size_y
            )
        count_column += 1
        offset_x += size_x
    count_row += 1
    offset_y += size_y


# canvas.create_line(
#     50, 50,
#     200, 200,
#     fill='blue',
#     width=10
# )

# canvas.create_oval(
#     5, 5,
#     50, 50,
#     fill='green',
#     outline='white',
#     width=10
# )

# points = (
#     (5, 55),
#     (60, 70),
#     (200, 300)
# )

# canvas.create_polygon(
#     *points,
#     fill='white',
#     outline='red',
#     width=10
# )

# canvas.create_text(
#     350, 100,
#     text='привет, я Булат',
#     font="Arial 18"
# )


# img = Image.open('icon.ico')
# img = img.resize((50, 50))
# img = ImageTk.PhotoImage(img)

# canvas.create_image(
#     250, 250,
#     image=img
# )


root.mainloop()