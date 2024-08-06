# s.ab. ttk widgets have a more modern look than tk ones.
import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    # print(entry.get())  # easier way, s.ab. not efficient
    miles = entry_int.get()  # better
    conv_km = 1.609 * miles
    output_string.set(conv_km)

# window
# window = tk.Tk()
window = ttk.Window(themename="journal")
window.title("Demo miles to kilometres converter")
window.geometry("350x150")

# title
# "label" in tkinter is a word for "text"
title_label = ttk.Label(master=window, text="Miles to kilometres", font="Calibri 24 bold")
title_label.pack()  # actually place the text onto the widget

# input field - entry field with a button
input_frame = ttk.Frame(master=window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_int)
# s.ab. you need to pass the name of the function, but don't call it (convert())!
button = ttk.Button(master=input_frame, text="Convert", command=convert)
entry.pack(side="left", padx=5)
button.pack(side="left")
input_frame.pack(pady=10)

# output
output_string = tk.StringVar()
output_label = ttk.Label(
        master=window, 
        text="Output",
        font="Calibri 20", 
        textvariable=output_string)
output_label.pack(pady=5)

# run (main loop)
window.mainloop()
