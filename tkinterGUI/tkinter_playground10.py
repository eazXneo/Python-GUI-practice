import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext  # not a widget itself, contains other widgets (s.ab. like ttk?)

# setup
window = tk.Tk()
window.title("playground 10 - sliders")
# window.geometry("500x1000")

# slider
scale_float = tk.DoubleVar(value=15)
scale = ttk.Scale(
    window,
    command=lambda value: progress.stop(), 
    from_=0, 
    to=25,
    length=300, 
    orient = "horizontal",
    variable=scale_float)
scale.pack()

# progress bar
progress = ttk.Progressbar(
        window, 
        variable=scale_float, 
        maximum=25,
        orient="horizontal",
        mode="indeterminate",
        length=350)
progress.pack()

progress.start(1000)  # s.ab don't use this apparently
progress.stop()

# scrolledtext
scrolled_text = scrolledtext.ScrolledText(window, width=100, height=7)
scrolled_text.pack()

my_progress_var = tk.IntVar()
my_progress = ttk.Progressbar(
        window,
        variable=my_progress_var,
        maximum=100,
        orient="vertical",
        mode="determinate",
        length=200)
my_progress.pack()
my_progress.start()

# (WIT) s.ab. becomes a ".0" float that is rounded down.
my_label = ttk.Label(window, textvariable=my_progress_var)
my_label.pack()

my_slider = ttk.Scale(
        window,
        from_=0,
        to=100,
        variable=my_progress_var)
my_slider.pack()

# run
window.mainloop()