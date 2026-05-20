import tkinter as tk


def show_checkbox_status():
    print(chekbox_status.get())
    
    
def show_radiobutton_status():
    print(radiobutton_status.get())


root = tk.Tk()


chekbox_status = tk.StringVar()

radiobutton_status = tk.IntVar()


radio_btns = [
    ('Кнопка 1', 1),
    ('Кнопка 2', 2),
    ('Кнопка 3', 3)
]


for text, value in radio_btns:
    tk.Radiobutton(text=text,
                   value=value,
                   command=show_radiobutton_status,
                   variable=radiobutton_status).pack()


btn = tk.Checkbutton(text="Вы согласны?", 
                     variable=chekbox_status,
                     command=show_checkbox_status,
                     onvalue='Нажата',
                     offvalue='Не нажата')
btn.pack()


root.mainloop()
