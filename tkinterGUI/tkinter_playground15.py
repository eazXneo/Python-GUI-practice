import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.title("playground 15 - layouts")
window.geometry("600x400")

# widgets
label1 = tk.Label(window, text="Label 1", background="red")  # ignore colours on a Mac (unless tk!)
label2 = tk.Label(window, text="Label 2", background="blue")

# pack
# TODO: useful to fully understand the difference between "expand" and "fill"
# label1.pack(side="left", expand=True, fill="both")
# label2.pack(side="left", expand=True)

# :) fun until here.

# grid
# window.columnconfigure(0, weight=1)
# window.columnconfigure(1, weight=1)
# window.columnconfigure(2, weight=2)
# window.rowconfigure(0, weight=1)
# window.rowconfigure(1, weight=1)

# label1.grid(row=0, column=1, sticky="nesw")
# label2.grid(row=1, column=1, columnspan=2, sticky="nswe")

# place
label1.place(x=100, y=200, width=200, height=100)
label2.place(relx=0.5 , rely=0.5, relwidth=1, anchor="se")

# run
window.mainloop()