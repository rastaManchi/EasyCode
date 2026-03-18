import tkinter as tk

root = tk.Tk()
root.title("NewApp")
root.geometry('500x500')
root.iconbitmap('icon.ico')

label = tk.Label(text="Привет, мир!")
label.pack()

entry = tk.Entry(borderwidth=2, cursor="hand2", relief="raised")
entry.pack()

root.mainloop()
