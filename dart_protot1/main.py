import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

import os

# TODO: relpath saving? 1
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class App(tk.Tk):
    def __init__(self):
        # setup
        super().__init__()
        self.geometry("1000x600")
        self.title("DART prototype 1")

        self.minsize(800,500)
        self.configure(bg="darkgrey")  # DEBUG: need borders for now 

        # layout
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0, weight=6)
        self.columnconfigure(1, weight=2)

        # widgets
        # Create left and right frames
        left_frame  =  ttk.Frame(self, width=650,  height=400)
        left_frame.grid(row=0,  column=0, rowspan=3,  padx=10,  pady=10)
        right_frame  =  ttk.Frame(self, width=650,  height=400)
        right_frame.grid(row=0,  column=1, rowspan=3, padx=10,  pady=10)

        right_frame_top  =  ttk.Frame(right_frame, width=200,  height=200)
        right_frame_top.grid(row=0,  column=1,  padx=10,  pady=25)
        right_frame_middle  =  ttk.Frame(right_frame, width=200,  height=400)
        right_frame_middle.grid(row=1,  column=1,  padx=10,  pady=25)
        right_frame_bottom  =  ttk.Frame(right_frame, width=200,  height=200)
        right_frame_bottom.grid(row=2,  column=1,  padx=10,  pady=25)

        # Create frames and labels
        ttk.Label(left_frame,  text="Image (/folder) selected: ").grid(row=0,  column=0,  padx=5,  pady=5)
        
        self.image = Image.open(resource_path("01_training.tif"))  # TODO: relpath saving? 2
        # resized_image = self.image.resize((650, 400))
        self.image_tk = ImageTk.PhotoImage(self.image)

        ttk.Label(left_frame,  image=self.image_tk).grid(row=1,  column=0,  padx=5,  pady=5)
        # Label(right_frame,  image=self.image_tk,  bg='grey').grid(row=0,  column=0,  padx=5,  pady=5)

        def clicked():
            '''if button is clicked, display message'''
            print("Clicked.")

        # For now, when the buttons are clicked, they only call the clicked() method. We will add functionality later.
        ttk.Button(right_frame_top,  text="Select image (/ folder)",  command=clicked).grid(row=0,  column=0,  padx=5,  pady=5,  sticky='w'+'e'+'n'+'s')

        # Example labels that serve as placeholders for other widgets
        ttk.Label(right_frame_middle,  text="Crop edges",  relief="raised").grid(row=0,  column=0,  padx=5,  pady=3,  ipadx=10)
        ttk.Label(right_frame_middle,  text="other toggle",  relief="raised").grid(row=0,  column=1,  padx=5,  pady=3,  ipadx=10)
        ttk.Label(right_frame_middle,  text="export options",  relief="raised").grid(row=1,  column=1,  padx=5,  pady=3,  ipadx=10)

        # tk.Button(tool_bar,  text="Select csv output location",  command=clicked).grid(row=2,  column=0,  padx=5,  pady=5,  sticky='w'+'e'+'n'+'s')
        # tk.Button(tool_bar,  text="(select output file type)",  command=clicked).grid(row=2,  column=1,  padx=5,  pady=5,  sticky='w'+'e'+'n'+'s')
       
        # tk.Button(tool_bar,  text="Black &amp; White",  command=clicked).grid(row=1,  column=1,  padx=5,  pady=5,  sticky='w'+'e'+'n'+'s')

        ttk.Button(right_frame_bottom,  text="Calculate DART value",  command=clicked).grid(row=0,  column=0,  padx=5,  pady=5,  sticky='w'+'e'+'n'+'s')
        ttk.Label(right_frame_bottom, text="DART VALUE: ", font="30").grid(row=1,  column=0,  padx=5,  pady=5)

        # run
        self.mainloop()

App()

# TODO: all toggles should be one class.