import tkinter as tk


root = tk.Tk()
root.title("MyApp")
root.geometry("400x400")
# root.iconbitmap("i.webp")


label = tk.Label(text="Hello world!")
label.pack()


root.mainloop()