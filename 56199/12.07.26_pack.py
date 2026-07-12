import tkinter as tk


# Создаем главное окно
root = tk.Tk()
root.title("Демонстрация pack()")
root.geometry("500x500")


# Несколько кнопок с разными параметрами pack()


# По умолчанию (верхний край окна)
btn_default = tk.Button(root, text="Default", bg="cyan")
btn_default.pack()


# Слева
btn_left = tk.Button(root, text="Left", bg="yellow")
btn_left.pack(side=tk.LEFT)


# Справа
btn_right = tk.Button(root, text="Right", bg="magenta")
btn_right.pack(side=tk.RIGHT)


# Сверху
btn_top = tk.Button(root, text="Top", bg="green")
btn_top.pack(side=tk.TOP)


# Снизу
btn_bottom = tk.Button(root, text="Bottom", bg="red")
btn_bottom.pack(side=tk.BOTTOM)


# Растягиваем по горизонтали
btn_fill_x = tk.Button(root, text="Fill X", bg="grey")
btn_fill_x.pack(fill=tk.X)


# Растягиваем по вертикали
btn_fill_y = tk.Button(root, text="Fill Y", bg="orange")
btn_fill_y.pack(fill=tk.Y)


# Растягиваем по обеим осям
btn_fill_both = tk.Button(root, text="Fill Both", bg="brown")
btn_fill_both.pack(fill=tk.BOTH, expand=True)


# Запускаем цикл обработки событий
root.mainloop()
