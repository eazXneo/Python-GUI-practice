# creating widgets for image import and output
import customtkinter as ctk
from tkinter import filedialog, Canvas
from settings import *


class ImageImport(ctk.CTkFrame):
    # cover entire entire window
    # it should contain a single button right in the middle
    # the button should say "open image"
    def __init__(self, parent, import_func):
        super().__init__(master=parent)
        # in main 2 columns specified, so here we need to "cover" the whole 
        # space with columnspan=2
        self.grid(column=0, columnspan=2, row=0, sticky="nsew")
        self.import_func = import_func
        ctk.CTkButton(master=self, text="open image", command=self.open_dialog).pack(expand=True)

        # my try
        # frame = ctk.CTkFrame(master=parent)
        # button = ctk.CTkButton(master=frame, text="open image")
        # button.pack()

    def open_dialog(self):
        path = filedialog.askopenfile().name
        self.import_func(path)


class ImageOutput(Canvas):
    def __init__(self, parent, resize_image):
        # can get rid of the last 3 args
        # tkinter default colour
        super().__init__(master=parent, background=BACKGROUND_COLOR, bd=0, highlightthickness=0, relief="ridge")
        self.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        # TODO: WIT !!!
        self.bind("<Configure>", resize_image)


# s.ab. only showing the close button when showing an image. So in this file.
class CloseOutput(ctk.CTkButton):
    def __init__(self, parent, close_func):
        super().__init__(
                master=parent,
                command=close_func,
                text="x", 
                text_color=WHITE, 
                fg_color="transparent", 
                width=40, 
                height=40,
                corner_radius=0.05,
                hover_color=CLOSE_RED)
        # TODO: relx and rely look really useful
        self.place(relx=0.99, rely=0.01, anchor="ne")
