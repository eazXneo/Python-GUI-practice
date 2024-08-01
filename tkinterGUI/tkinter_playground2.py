import tkinter as tk
from tkinter import ttk

# count = 0

def button_func():
    # count += 1

    # get the content of the entry
    # print(entry.get())
    entry_text = entry.get()

    # update label
    # label.configure(text="new text!")
    # label["text"] = "new text!" if (count%2 == 0) else "l (old text)"
    label["text"] = "You typed: " + entry_text
    entry["state"] = "disabled"

    # TODO: useful info
    # print(label.configure())

def reset_func():
    label["text"] = "some text"
    entry["state"] = "enabled"

window = tk.Tk()
window.title("playground 2 - data")
# window.geometry("300x500")

label = ttk.Label(master=window, text="l")
label.pack()

entry = ttk.Entry(master=window)
entry.pack()

button = ttk.Button(master=window, text="The button", command=button_func)
button.pack()

# reset button
reset_button = ttk.Button(master=window, text="press here to reset", command=reset_func)
reset_button.pack()

window.mainloop()