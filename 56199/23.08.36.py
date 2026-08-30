import tkinter as tk
from tkinter.messagebox import showinfo


def send():
    text = entry.get()
    print(text)

root = tk.Tk()

entry = tk.Entry()
entry2 = tk.Entry()

label = tk.Label(text="Имя:")
label2 = tk.Label(text="Фамилия: ")

label.pack()
entry.pack()

label2.pack()
entry2.pack()

btn = tk.Button(text='Отправить', command=send)
btn.pack()

root.mainloop()