import tkinter as tk


def append_to_label(value):
    current_text = input_panel.get()
    input_panel.set(current_text + value)


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

input_panel = tk.Entry()
input_panel.grid(row=0, column=0, columnspan=4)


column = 0
row = 1
for struct_row in struct:
    for item in struct_row:
        tk.Button(text=item, 
                  padx=20, 
                  pady=20,
                  command=lambda: append_to_label(item)).grid(column=column, row=row)
        column += 1
    column = 0
    row += 1


root.mainloop()