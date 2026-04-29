import tkinter as tk 
from tkinter import ttk

root = tk.Tk()
root.title("")
root.geometry('500x500')

main_menu = tk.Menu()


FirstMenu = tk.Menu(main_menu, tearoff = 0) 
main_menu.add_cascade(label = "69", menu=FirstMenu)

SecondMenu = tk.Menu(main_menu, tearoff=0)
FirstMenu.add_cascade(label = "68", menu=SecondMenu)

ThirdMenu = tk.Menu(main_menu, tearoff=0)
SecondMenu.add_cascade(label = "67", menu=ThirdMenu)


root.config(menu = main_menu)


canvas = tk.Canvas(
    bg='blue',
    width=250,
    height=250
)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

for i in range(50, 550, 50):
    canvas.create_text(50, i, text=f"{i}", font="Arial 20")
    
scrollbar = ttk.Scrollbar(orient="vertical", command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)


root.mainloop()