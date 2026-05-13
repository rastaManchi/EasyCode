import tkinter as tk
from tkinter.messagebox import showerror


def append_to_expression(value):
    current_text = result_var.get()
    result_var.set(current_text + value)
    

def clear():
    result_var.set("")
    
def validate_expression(expression: str):
    text = expression.replace('/', '').replace('*', '').replace('+', '').replace('-', '')
    return text.isdigit()
    
def calculate():
    try:
        expression = result_var.get()
        if not expression:
            showerror('Ошибка', 'поле для ввода не должно быть пустым')
        expression = expression.replace('x', '*').replace('÷', '/')
        if validate_expression(expression):
            result = eval(expression)
            result_var.set(result)
        else:
            showerror('Ошибка', 'Замечена подозрительная активность')
    except ZeroDivisionError:
        showerror('Ошибка', 'Делить на ноль нельзя')
        clear()


root = tk.Tk()
root.geometry('400x400')


buttons = [
    '7', '8', '9', '÷',
    '4', '5', '6', 'x',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]


for x in range(5):
    for y in range(4):
        root.columnconfigure(y, weight=1)
        root.rowconfigure(x, weight=1)
        
result_var = tk.StringVar()

entry = tk.Entry(font=('Arial', 24), width=14, borderwidth=4, textvariable=result_var)
entry.grid(row=0, column=0, columnspan=4)

row_val = 1
col_val = 0

for button in buttons:
    if button == 'C':
        btn = tk.Button(text=button, font=('Arial', 18), padx=20, pady=20, command=clear)
    elif button == '=':
        btn = tk.Button(text=button, font=('Arial', 18), padx=20, pady=20, command=calculate)
    else:
        btn = tk.Button(text=button, font=('Arial', 18), padx=20, pady=20, command=lambda btn=button: append_to_expression(btn))
    btn.grid(row=row_val, column=col_val)
    col_val += 1
    
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
