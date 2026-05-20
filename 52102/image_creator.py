import tkinter as tk


current_shape = 'line'
start_x = None
start_y = None
canvas = None


def set_shape(shape):
    global current_shape
    current_shape = shape
    
    
def on_btn_press(event):
    global start_x, start_y
    start_x, start_y = event.x, event.y
    

def on_mouse_drag(event):
    global start_x, start_y
    canvas.delete('temp')
    if current_shape == 'line':
        canvas.create_line(start_x, start_y, event.x, event.y, tags='temp')
    elif current_shape == 'rectangle':
        canvas.create_rectangle(start_x, start_y, event.x, event.y, tags='temp')
    elif current_shape == 'circle':
        r = ((event.x - start_x) ** 2 + (event.y - start_y) ** 2) ** 0.5
        canvas.create_oval(start_x - r, start_y - r, start_x + r, start_y + r, tags='temp')
        
        

def on_mouse_release(event):
    global start_x, start_y
    if current_shape == 'line':
        canvas.create_line(start_x, start_y, event.x, event.y)
    elif current_shape == 'rectangle':
        canvas.create_rectangle(start_x, start_y, event.x, event.y)
    elif current_shape == 'circle':
        r = ((event.x - start_x) ** 2 + (event.y - start_y) ** 2) ** 0.5
        canvas.create_oval(start_x - r, start_y - r, start_x + r, start_y + r)
        
        
def reset():
    canvas.delete('all')


root = tk.Tk()
root.title('Рисовашка')


canvas = tk.Canvas(bg='gray', height=600, width=800)
canvas.bind('<Button-1>', on_btn_press)
canvas.bind('<B1-Motion>', on_mouse_drag)
canvas.bind('<ButtonRelease-1>', on_mouse_release)
canvas.pack()

frame = tk.Frame()
frame.pack()

circle_btn = tk.Button(frame, text='Круг', command=lambda shape='circle': set_shape(shape))
circle_btn.pack(side=tk.LEFT)

rect_btn = tk.Button(frame, text='Прямоугольник', command=lambda shape='rectangle': set_shape(shape))
rect_btn.pack(side=tk.LEFT)

line_btn = tk.Button(frame, text='Линия', command=lambda shape='line': set_shape(shape))
line_btn.pack(side=tk.LEFT)

reset_btn = tk.Button(frame, text='Очистить', command=reset)
reset_btn.pack(side=tk.LEFT)

root.mainloop()
