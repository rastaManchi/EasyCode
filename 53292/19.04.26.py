import tkinter as tk 

root = tk.Tk()

root.title('MyAPP')
root.geometry("500x500")
root.iconbitmap('icon.ico')

label = tk.Label(text='Привет мир!', foreground="#2AC9AC")
label.pack()

root.mainloop()