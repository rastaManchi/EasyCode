import tkinter as tk
from tkinter.messagebox import  showinfo, \
                                showwarning, \
                                showerror, \
                                askyesno

showinfo('Какая-то информация', '...')
showwarning('Предупреждение', '...')
showerror('Какая-то ошибка', '...')
result = askyesno("Title", "text")
if result:
    print('Нажал да')
else:
    print('Нажал нет')

windowSettings1 = None
windowSettings2 = None

def open_settings():
    global windowSettings1
    if not windowSettings1:
        windowSettings1 = tk.Tk()
        windowSettings1.title('Settings')

def close_settings():
    global windowSettings1
    if windowSettings1:
        windowSettings1.destroy()
    windowSettings1 = None


def open_settings2():
    global windowSettings2
    if not windowSettings2:
        windowSettings2 = tk.Tk()
        windowSettings2.title('Settings')

def close_settings2():
    global windowSettings2
    if windowSettings2:
        windowSettings2.destroy()
    windowSettings2 = None


root = tk.Tk()
root.title('root')

main_menu = tk.Menu()
main_menu.add_command(label="Settings", command=open_settings)
main_menu.add_command(label="CloseSettings", command=close_settings)
main_menu.add_command(label="Settings2", command=open_settings2)
main_menu.add_command(label="CloseSettings2", command=close_settings2)

root.config(menu=main_menu)

root.mainloop()