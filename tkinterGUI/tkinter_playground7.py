import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.title("playground 7 - combobox and spinbox")
window.geometry("500x500")

# combobox
items = ("Ice cream", "Pizza", "Broccoli")
food_string = tk.StringVar(value=items[0])
combo = ttk.Combobox(window, textvariable=food_string)
combo["values"] = items  # recommended
# combo.configure(values=items)
combo.pack()

# events
combo.bind("<<ComboboxSelected>>", lambda event: print(food_string.get()))
combo_label = ttk.Label(window, text="a label", textvariable=food_string)
combo_label.pack()

# run
window.mainloop()