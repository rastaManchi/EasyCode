import tkinter as tk


clicks = 0


def click():
    global clicks
    clicks += 1
    button['text'] = f"{clicks}"
    button['background'] = "#ff0000"
    root.after(2000, reset_text)
    
    
def reset_text():
    button['text'] = 'Нажми на меня'
    button['background'] = "#ffffff"


root = tk.Tk()


button = tk.Button(text='Нажми на меня', relief='solid', command=click)
button.pack()


root.mainloop()