import tkinter as tk
from tkinter import ttk

def get_pos(event):
    print(f"x: {event.x} y: {event.y}")

# setup
window = tk.Tk()
window.title("playground 6 - event binding")
window.geometry("400x500")

# widgets
text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

button = ttk.Button(window)
button.pack()

# events
# window.bind('<Control-z>', lambda event: print("an event happened"))
# window.bind('<Control-z>', lambda event: print(event))
# button.bind('<Control-z>', lambda event: print(event))
# window.bind('<KeyPress>', lambda event: print(f'a button was pressed ({event.char})'))
# window.bind("<Motion>", get_pos)
# text.bind("<Motion>", get_pos)

# check if user has selected the user field
entry.bind("<FocusIn>", lambda event: print('entry field was selected'))
entry.bind("<FocusOut>", lambda event: print("entry field was UN-selected"))

text.bind("<Shift-MouseWheel>", lambda event: print("Mousewheel"))

# run
window.mainloop()

### script found at https://python-course.eu/tkinter/events-and-binds-in-tkinter.php ###
#!/usr/bin/python3
# write tkinter as Tkinter to be Python 2.x compatible
"""
from tkinter import *
def hello(event):
    print("Single Click, Button-l") 
def quit(event):                           
    print("Double Click, so let's stop") 
    import sys; sys.exit() 

widget = Button(None, text='Mouse Clicks')
widget.pack()
widget.bind('<Button-1>', hello)
widget.bind('<Double-1>', quit) 
widget.mainloop()
"""