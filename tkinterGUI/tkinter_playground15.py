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
label1.pack(side="left", expand=True, fill="both")
label2.pack(side="left")

# run
window.mainloop()