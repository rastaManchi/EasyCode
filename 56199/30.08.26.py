import tkinter as tk


def append_to_label(value):
    current_text = result.get()
    result.set(current_text + value)


def clear_input():
    result.set("")


def get_result():
    math_result = eval(result.get())
    result.set(math_result)


root = tk.Tk()


for x in range(5):
    for y in range(4):
        root.columnconfigure(y, weight=1) 
        root.rowconfigure(x, weight=1)

struct = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '+'],
    ['C', '0', '=', '-']
]

result = tk.StringVar()

input_panel = tk.Entry(textvariable=result)
input_panel.grid(row=0, column=0, columnspan=4)


column = 0
row = 1
for struct_row in struct:
    for item in struct_row:
        if item == 'C':
            tk.Button(text=item, 
                        padx=20, 
                        pady=20,
                        command=clear_input).grid(column=column, row=row)
        elif item == '=':
            tk.Button(text=item, 
                        padx=20, 
                        pady=20,
                        command=get_result).grid(column=column, row=row)
        else:
            tk.Button(text=item, 
                    padx=20, 
                    pady=20,
                    command=lambda text=item: append_to_label(text)).grid(column=column, row=row)
        column += 1
    column = 0
    row += 1


root.mainloop()