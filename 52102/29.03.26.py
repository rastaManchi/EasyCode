import tkinter as tk

root = tk.Tk()
root.geometry('500x500')


for x in range(4):
    for y in range(3):
        root.columnconfigure(y, weight=1)
        root.rowconfigure(x, weight=1)


btn1 = tk.Button(text='1', bg='black')
btn1.grid(column=0, row=0, sticky='nsew')


btn2 = tk.Button(text='2', bg='black')
btn2.grid(column=2, row=0, sticky='nsew')


btn3 = tk.Button(text='1', bg='black')
btn3.grid(column=1, row=1, sticky='nsew')


btn4 = tk.Button(text='1', bg='black')
btn4.grid(column=0, row=2, sticky='nsew')


btn5 = tk.Button(text='2', bg='black')
btn5.grid(column=2, row=2, sticky='nsew')


btn6 = tk.Button(text='1', bg='black')
btn6.grid(column=1, row=3, sticky='nsew')


root.mainloop()