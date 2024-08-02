import customtkinter as ctk
from settings import *

class Panel(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color=DARK_GREY)
        self.pack(fill="x", pady=4, ipady=8)

class SliderPanel(Panel):
    def __init__(self, parent, text):
        super().__init__(parent=parent)

        ctk.CTkLabel(self, text=text)
        # create slider box.
        # the grid
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        # the elements
        name_label = ctk.CTkLabel(self, text=text)
        name_label.grid(column=0, row=0, sticky="w", padx=5, pady=5)

        slider_val_label = ctk.CTkLabel(self, text="0.0")
        slider_val_label.grid(column=0, row=0, sticky="e", padx=5, pady=5)

        slider_pl = ctk.CTkLabel(self, text="imagine a slider here...")
        slider_pl.grid(column=0, row=1, sticky="we", padx=5, pady=5)