import tkinter as tk 

root = tk.Tk()

root.title('MyAPP')
root.geometry("500x500")
root.iconbitmap('icon.ico')

# Конфигурируем сетку
for x in range(2):
    for y in range(2):
        root.columnconfigure(y, weight=1)
        root.rowconfigure(x, weight=1)

label = tk.Label(text='Привет мир!', foreground="#2AC9AC", background="black")
# label.pack(side="bottom", fill='x', padx=100)
# label.place(relx=0.5, rely=0.5, relwidth=0.4)
label.grid(row=1)


btn = tk.Button(background='black')

root.mainloop()