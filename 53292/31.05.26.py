import tkinter as tk
from tkinter import ttk


root = tk.Tk()

canvas = tk.Canvas(
    bg='gray',
    width=250,
    height=250
)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

for i in range(50, 550, 50):
    canvas.create_text(50, i, text=f"{i}", font='Arial 20')
    
    
scrollbar = ttk.Scrollbar(orient='vertical', command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill="y")

canvas.configure(yscrollcommand=scrollbar.set)

root.mainloop()