import tkinter as tk


# Создаем главное окно
root = tk.Tk()
root.title("Демонстрация place()")
root.geometry("500x500")


# Несколько кнопок с различными способами размещения методом place()


# Стандартное позиционирование по координатам
btn_at_position = tk.Button(root, text="At Position (100, 100)", bg="cyan")
btn_at_position.place(x=100, y=100)


# Центр экрана
btn_centered = tk.Button(root, text="Centered", bg="yellow")
btn_centered.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


# Верхний правый угол
btn_top_right = tk.Button(root, text="Top Right Corner", bg="magenta")
btn_top_right.place(relwidth=0.3, relheight=0.1, relx=0.7, rely=0)


# Нижний левый угол
btn_bottom_left = tk.Button(root, text="Bottom Left Corner", bg="green")
btn_bottom_left.place(width=150, height=50, x=0, rely=1, anchor=tk.SW)


# Растяжение по ширине окна
btn_stretch_width = tk.Button(root, text="Stretch Width", bg="red")
btn_stretch_width.place(y=200, relwidth=1)


# Растяжение по высоте окна
btn_stretch_height = tk.Button(root, text="Stretch Height", bg="orange")
btn_stretch_height.place(x=300, relheight=1)




root.mainloop()
