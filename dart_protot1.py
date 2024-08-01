import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        # setup
        super().__init__()
        self.geometry("1000x600")
        self.title("DART prototype 1")

        self.minsize(800,500)

        # layout
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=6)

        # widgets
        # ImportButton (Frame with a button), TODO: why?
        # self.image_import = ImageImport(self, self.import_image)

        # run
        self.mainloop()

App()