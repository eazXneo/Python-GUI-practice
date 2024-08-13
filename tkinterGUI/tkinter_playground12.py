import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.title("playground 12 - tabs")
window.geometry("500x350")

# tab widget (notebook)
notebook = ttk.Notebook(window)

# tab 1
tab1 = ttk.Frame(window)  # can be window if wanted.
label1 = ttk.Label(tab1, text="Text")
label1.pack()
button1 = ttk.Button(tab1, text="Button in tab 1")
button1.pack()

# tab 2
tab2 = ttk.Frame(notebook)
label2 = ttk.Label(tab2, text="new text!")
label2.pack()
entry2 = ttk.Entry(tab2)
entry2.pack()

# exercise:
tab3 = ttk.Frame(notebook)
btn2 = ttk.Button(tab3, text="fun btn")
btn2.pack()
btn3 = ttk.Button(tab3, text="boring")
btn3.pack()
label3 = ttk.Label(tab3, text="gogogo")
label3.pack()

notebook.add(tab1, text="tab 1")
notebook.add(tab2, text="tab 2")
notebook.add(tab3, text="exercise tab")
notebook.pack()

# run
window.mainloop()