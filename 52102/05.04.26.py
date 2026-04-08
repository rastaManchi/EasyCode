import tkinter as tk

root = tk.Tk()
root.title("Омэрэканский бургэр")
root.geometry('500x500')

nachinki =(
    'Помидоры,'
    'Огурец,'
   'Листья_салата,'
    'Бекон,'
    'Сыр,'
    'Лук,'
    'Котлета'
)

def showburger():
    burger = []
    if meat.get():
        burger.append('Котлета')
    if tomato.get():
        burger.append('Помидор')
    print(burger)



meat = tk.BooleanVar()
tomato = tk.BooleanVar()

tk.Checkbutton(
    text='Котлета',
    variable=meat,
    onvalue=True,
    offvalue=False).pack()

tk.Checkbutton(
    text='Помидор',
    variable=tomato,
    onvalue=True,
    offvalue=False).pack()


btn = tk.Button(text='...', command=showburger)
btn.pack()

root.mainloop()