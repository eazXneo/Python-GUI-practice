import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.title("playground 11 - frames and parenting")
# window.geometry("600x400")

# frame
frame = ttk.Frame(window, width=175, height=80, borderwidth=7, relief=tk.GROOVE)
frame.pack_propagate(False)
frame.pack(side="left")

# master setting
label = ttk.Label(frame, text="Label in frame")
label.pack()

button = ttk.Button(frame, text="button in a frame")
button.pack()

# example
label2 = ttk.Label(window, text="Label outside frame")
label2.pack(side="left")

# exercise
my_frame = ttk.Frame(window, relief=tk.GROOVE)

ttk.Label(my_frame, text="my label").pack()
ttk.Button(my_frame, text="a btn").pack()
ttk.Entry(my_frame).pack()

my_frame.pack(side="left")

# run
window.mainloop()