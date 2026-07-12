import tkinter as tk


# Создаем главное окно
root = tk.Tk()
root.title("Демонстрация grid()")
root.geometry("500x500")


# Конфигурируем сетку
for x in range(2):
    for y in range(2):
        root.columnconfigure(y, weight=1)
        root.rowconfigure(x, weight=1)


# Верхний левый квадрат
btn_topleft = tk.Button(root, text="Верхний Левый", bg="cyan")
btn_topleft.grid(row=0, column=0, sticky="nsew")


# Верхний правый квадрат
btn_topright = tk.Button(root, text="Верхний Правый", bg="yellow")
btn_topright.grid(row=0, column=1, sticky="nsew")


# Нижний левый квадрат
btn_bottomleft = tk.Button(root, text="Нижний Левый", bg="magenta")
btn_bottomleft.grid(row=1, column=0, sticky="nsew")


# Нижний правый квадрат
btn_bottomright = tk.Button(root, text="Нижний Правый", bg="green")
btn_bottomright.grid(row=1, column=1, sticky="nsew")


# Запускаем цикл обработки событий
root.mainloop()
