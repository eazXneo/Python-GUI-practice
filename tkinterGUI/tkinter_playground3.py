import tkinter as tk
from tkinter import ttk

def button_func():
    pass

window = tk.Tk()
window.title("playground 2 - variables")
window.geometry("300x100")

# tkinter variable
string_var = tk.StringVar()
# connect it to label and entry to automatically get and set these at the same(-ish) time

label = ttk.Label(master=window, text="l", textvariable=string_var)
label.pack()

entry = ttk.Entry(master=window, textvariable=string_var)
entry.pack()

# button = ttk.Button(master=window, text="button", command=button_func)
# button.pack()

window.mainloop()