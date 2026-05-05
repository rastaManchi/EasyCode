import tkinter as tk


clicks = 0

def click():
    global clicks
    clicks += 1
    label['text'] = f"Кол-во кликов: {clicks}"
    btn['background'] = 'green'
    root.after(2000, reset_btn)
    
    
def reset_btn():
    btn['background'] = 'white'


root = tk.Tk()

label = tk.Label(text=f"Кол-во кликов: {clicks}")
label.pack()

btn = tk.Button(text='Нажми на меня',
                foreground='gray',
                command=click)
btn.pack()


root.mainloop()

