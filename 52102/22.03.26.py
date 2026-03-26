import tkinter as tk
import subprocess
import random


clicks = 0


def click_listener():
    global clicks
    clicks += 1
    btn['text'] = f"{clicks}"
    result = subprocess.run('python 08.03.26.py')
    root.after(2000, default_btn)


def default_btn():
    btn['text'] = "Нажми на меня"
    btn['background'] = f'#{random.randint(0, 255):02X}{random.randint(0, 255):02X}{random.randint(0, 255):02X}' 


root = tk.Tk()
root.title("NewApp")
root.geometry('500x500')
root.iconbitmap('icon.ico')

btn = tk.Button(text="Нажми на меня",
                borderwidth=3,
                relief='solid',
                background='gray',
                foreground='white',
                command=click_listener
                )
btn.pack()

root.mainloop()