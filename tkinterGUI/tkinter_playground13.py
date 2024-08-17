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
file_menu.add_separator()  # Mac issue? Kind of, Mac doesn't seem to allow a trailing separator
file_menu.add_command(label="Open", command=lambda: print("Open file"))
menu.add_cascade(label="File", menu=file_menu)

# another sub-menu
help_menu = tk.Menu(menu, tearoff=False)
help_menu.add_command(label="Help entry", command=lambda: print(help_check_string.get()))
help_check_string = tk.StringVar()
help_menu.add_checkbutton(label="check", onvalue="on", offvalue="off", variable=help_check_string)
menu.add_cascade(label="Help", menu=help_menu)

# exercise
# docs: https://www.tutorialspoint.com/python/tk_menu.htm
# my sub menu
confused_menu = tk.Menu(menu, tearoff=False)
# seems to work with the master=menu as well... TODO Why?

clarity_menu = tk.Menu(confused_menu, tearoff=False)  
clarity_menu.add_command(label="Clarify", command=lambda: print("All clear now!"))

menu.add_cascade(label="Confused", menu=confused_menu)
confused_menu.add_cascade(label="Clarity", menu=clarity_menu)

window.configure(menu=menu)

# menu button
menu_button = ttk.Menubutton(window, text="Menu Button")
menu_button.pack()

button_sub_menu = tk.Menu(menu_button, tearoff=False)
button_sub_menu.add_command(label="entry 1", command=lambda: print("entry 1"))
button_sub_menu.add_checkbutton(label="check 1")
# menu_button.configure(menu=button_sub_menu)
menu_button["menu"] = button_sub_menu  # same as above

# run
window.mainloop()