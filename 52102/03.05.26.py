import tkinter as tk
from tkinter.messagebox import *


def get_values():
    name = name_entry.get()
    surname = surname_entry.get()
    age = age_entry.get()
    msg = message_entry.get()
    flag = True
    
    if not all([name, surname, age, msg]):
        showerror('Value Error', 'Все поля должны быть заполнены!')
        flag = False
    
    if age.isdigit():
        if int(age) < 12:
            showerror('Age Error', 'Возраст должен быть не меньше 12 лет!')
            flag = False
    else:
        showerror('Age Error', 'Возраст нужно указать цифрами!')
        flag = False
        
    if len(msg) > 50:
        showerror('Message Error', 'Поле сообщения не должно превышать 50 символов!')
        flag = False
        
    if flag:
        print(f"{name} - {surname} - {age} - {msg}")


root = tk.Tk()


tk.Label(text='Имя: ').grid(row=0, column=0)
name_entry = tk.Entry(relief='solid')
name_entry.grid(row=0, column=1)


tk.Label(text="Фамилия: ").grid(row=1, column=0)
surname_entry = tk.Entry(relief='solid')
surname_entry.grid(row=1, column=1)


# Поле ВОЗРАСТ
tk.Label(text="Возраст: ").grid(row=2, column=0)
age_entry = tk.Entry(relief='solid')
age_entry.grid(row=2, column=1)


# Поле СООБЩЕНИЕ
tk.Label(text="Сообщение: ").grid(row=3, column=0)
message_entry = tk.Entry(relief='solid')
message_entry.grid(row=3, column=1)


btn = tk.Button(text='Отправить',
                padx=10,
                pady=2,
                command=get_values)
btn.grid(row=4, columnspan=2)

root.mainloop()
