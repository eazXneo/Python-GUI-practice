import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.title("playground 14 - more about windows")

# exercise - place window in middle of screen
win_width = 600
win_height = 400
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_pos = int((screen_width / 2) - (win_width / 2))
y_pos = int((screen_height / 2) - (win_height / 2))

geometry_string = f"{win_width}x{win_height}+{x_pos}+{y_pos}"

window.geometry(geometry_string)
# TODO: something about icons, but seems different on a Mac

# window sizing
window.minsize(200, 100)
# window.maxsize(800, 700)
# window.resizable(True, False)

# screen attributes
print(window.winfo_screenwidth())
print(window.winfo_screenheight())

# window attributes
window.attributes("-alpha", 1) 
# window.attributes("-topmost", True)

# security event
window.bind("<Escape>", lambda event: window.quit())

# window.attributes("-disable", True)  # doesn't seem to exist on Mac / anymore
# window.attributes("-fullscreen", True)

# title bar
# window.overrideredirect(True)
# grip = ttk.Sizegrip(window)
# anchor specifies which point of the widget we are talking about in relx and rely
#  so "se" means the bottom-right corner for the grip widget.
# grip.place(relx=1.0, rely=1.0, anchor="se")  # doens't work :( TODO: Why?

# run
window.mainloop()