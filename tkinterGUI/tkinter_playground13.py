import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.title("playground 13 - menu")
window.geometry("500x350")

# menu
menu = tk.Menu(window)
# sub-menu
file_menu = tk.Menu(menu, tearoff=False)
file_menu.add_command(label="New", command=lambda: print("New file"))
file_menu.add_command(label="Open", command=lambda: print("Open file"))
file_menu.add_separator()  # Mac issue?
menu.add_cascade(label="File", menu=file_menu)

# another sub-menu
help_menu = tk.Menu(menu, tearoff=False)
help_menu.add_command(label="Help entry", command=lambda: print(help_check_string.get()))
help_check_string = tk.StringVar()
help_menu.add_checkbutton(label="check", onvalue="on", offvalue="off", variable=help_check_string)
menu.add_cascade(label="Help", menu=help_menu)

window.configure(menu=menu)

# menu button
menu_button = ttk.Menubutton(window, text="Menu Button")
menu_button.pack()
button_sub_menu = tk.Menu(menu_button, tearoff=False)

# run
window.mainloop()