import tkinter as tk
from tkinter import ttk

def button_func():
    print(string_var.get())
    string_var.set(value="button pressed")

window = tk.Tk()
window.title("playground 3 - variables")
window.geometry("300x200")

# tkinter variable
string_var = tk.StringVar(value="start value")
# connect it to label and entry to automatically get and set these at the same(-ish) time

label = ttk.Label(master=window, text="l", textvariable=string_var)
label.pack()

entry = ttk.Entry(master=window, textvariable=string_var)
entry.pack()

button = ttk.Button(master=window, text="button", command=button_func)
button.pack()

string_var1 = tk.StringVar(value="test")
entry1 = ttk.Entry(master=window, text="test", textvariable=string_var1)
entry1.pack()
entry2 = ttk.Entry(master=window, textvariable=string_var1)
entry2.pack()
label1 = ttk.Label(master=window, textvariable=string_var1)
label1.pack()

window.mainloop()