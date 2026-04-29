import tkinter as tk 
from tkinter.messagebox import *


window = None


def close_second_window():
    global window
    if window:
        result = askyesno('Are you sure?', 'Закрыть второе окно?')
        if result:
            window.destroy()
            window = None
    else:
        showinfo('Second Window', 'Sorry, second window not found!')


def create_second_window():
    global window
    if not window:
        window = tk.Tk()
        window.title('Second')
        label = tk.Label(window, text='Second')
        label.pack()
    else:
        showinfo('Second Window', 'Sorry, second window already started!')

# eurotrucks2.exe + 0x2CFA128 -> 0x10 -> 0x10

root = tk.Tk()
root.title('Main')


label2 = tk.Label(root, text='Main')
label2.pack()

btn_open = tk.Button(root, text='Открыть окно', command=create_second_window)
btn_open.pack()

btn = tk.Button(root, text='Закрыть окно', command=close_second_window)
btn.pack()

create_second_window()

root.mainloop()
