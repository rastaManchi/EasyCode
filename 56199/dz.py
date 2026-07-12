import tkinter as tk 


def first():
    button['background'] = "#003865"
    root.after(2000, second)
    
    
def second():
    button['background'] = "#6B0000"


root = tk.Tk()


button = tk.Button(text='Нажми на меня', bg="#6B0000", command=first)
button.pack()


root.mainloop()