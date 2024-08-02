import tkinter as tk
from tkinter import ttk

class ImageImport(ttk.Frame):
    """
    (Frame + Button) to import image and/or folder.
    Opens the file explorer dialog for election
    """
    def __init__(self, parent):
        super().__init__(master=parent)
        # TODO: cover entire RIGHT SIDE
        self.grid(row=0,  column=1,  padx=5,  pady=5,  sticky='nsew')

        # button, should say "select image (folder)"
        import_imgs_button = ttk.Button(master=self, text="select image(s)")
        import_imgs_button.pack(expand=True)
