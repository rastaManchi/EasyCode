import tkinter as tk

root = tk.Tk()
root.title('Красивое приложение')
root.geometry('600x600')
root.configure(bg='#1a1a2e')

for x in range(4):
    for y in range(3):
        root.columnconfigure(y, weight=1, minsize=150)
        root.rowconfigure(x, weight=1, minsize=120)

button_style = {
    'font': ('Arial', 18, 'bold'),
    'fg': 'white',
    'activeforeground': 'white',
    'relief': 'flat',
    'borderwidth': 0,
    'cursor': 'hand2'
}

btn1 = tk.Button(text='1', bg='#0f3460', activebackground='#16213e', **button_style)
btn1.grid(column=0, row=0, sticky='nsew', padx=10, pady=10)

btn2 = tk.Button(text='2', bg='#e94560', activebackground='#d63447', **button_style)
btn2.grid(column=2, row=0, sticky='nsew', padx=10, pady=10)

btn3 = tk.Button(text='1', bg='#0f3460', activebackground='#16213e', **button_style)
btn3.grid(column=1, row=1, sticky='nsew', padx=10, pady=10)

btn4 = tk.Button(text='1', bg='#0f3460', activebackground='#16213e', **button_style)
btn4.grid(column=0, row=2, sticky='nsew', padx=10, pady=10)

btn5 = tk.Button(text='2', bg='#e94560', activebackground='#d63447', **button_style)
btn5.grid(column=2, row=2, sticky='nsew', padx=10, pady=10)

btn6 = tk.Button(text='1', bg='#0f3460', activebackground='#16213e', **button_style)
btn6.grid(column=1, row=3, sticky='nsew', padx=10, pady=10)

root.mainloop()