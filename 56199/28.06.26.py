import tkinter as tk


root = tk.Tk()
root.title("MyApp")
root.geometry("400x400")
# root.iconbitmap("i.webp")


label = tk.Label(text="Hello world", foreground="red", background="#2CC655")
label.pack()


root.mainloop()