import tkinter as tk


root = tk.Tk()
root.title("MyApp")
root.geometry("400x400")
# root.iconbitmap("i.webp")


label = tk.Label(text="Hello world!")
label.pack()

root2 = tk.Tk()
root2.title("MyApp")
root2.geometry("400x400")
# root.iconbitmap("i.webp")


label = tk.Label(root2, text="Hello world!!")
label.pack()


root.mainloop()