import tkinter as tk

root = tk.Tk()
root.title("Омэрэканский бургэр")
root.geometry('500x500')

main_menu = tk.Menu()
global_menu = main_menu

for i in range(17):
    before_menu = main_menu
    main_menu = tk.Menu(before_menu, tearoff=0)
    main_menu.add_command(label='Test')
    before_menu.add_cascade(label="далее", menu=main_menu)

main_menu.add_command(label='о программе')
main_menu.add_command(label='выход')

root.config(menu=global_menu)
root.mainloop()