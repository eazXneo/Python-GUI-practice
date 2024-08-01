import tkinter as tk
from tkinter import ttk

def button_func():
    print("The button was pressed!")

def hello_func():
    print("hello")

# create a window
window = tk.Tk()
window.title("playground 1 - widgets")
window.geometry("800x500")

# ttk widget
label = ttk.Label(master=window, background="#ffffff", foreground="blue", text="this is a fun label")
label.pack()

# tk widget
text = tk.Text(master=window)
text.pack()

# dealing with Mac colour problems, but then makes buttons look Windows-like.
# style = ttk.Style(window)
# style.theme_use('classic')

entry = ttk.Entry(master=window)
entry.pack()

# text label 1
label1 = ttk.Label(master=window, text="my label")
label1.pack()
# button 1
# button_hello = ttk.Button(master=window, text="say hello", command=hello_func)
# lambda functions can be passed as command
button_hello = ttk.Button(master=window, text="say hello", command=lambda: print("hello"))
button_hello.pack()

button = ttk.Button(master=window, text="a button", command=button_func)
button.pack()

# run
window.mainloop()
print("I was blocked by the mainloop until now")

# --------------------------------------------- #
#                 tutorial end                  #
#        checking required elements             #
# --------------------------------------------- #