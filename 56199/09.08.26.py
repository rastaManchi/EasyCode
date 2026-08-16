import tkinter as tk


def test():
    print('Привет')


root = tk.Tk()


main_menu = tk.Menu()
main_menu.add_command(label="File", command=test)

edit_menu = tk.Menu(main_menu, tearoff=0)
edit_menu.add_command(label="Cancel")
edit_menu.add_command(label="Cut")
edit_menu.add_separator()
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
edit_menu.add_checkbutton(label='Autosave')

main_menu.add_cascade(label="Edit", menu=edit_menu)

root.config(menu=main_menu)


root.mainloop()
