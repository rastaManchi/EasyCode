import tkinter as tk

window = None

def open_settings():
    global window
    if not window:
        window = tk.Tk()
        window.title('Settings')

def close_settings():
    global window
    if window:
        window.destroy()
    window = None

root = tk.Tk()
root.title('root')

main_menu = tk.Menu()
main_menu.add_command(label="Settings", command=open_settings)
main_menu.add_command(label="CloseSettings", command=close_settings)

root.config(menu=main_menu)

root.mainloop()