import customtkinter as ctk
from panels import *

class Menu(ctk.CTkTabview):  # a frame with tabs
    def __init__(self, parent):
        super().__init__(master=parent)
        self.grid(row=0, column=0, sticky="nsew")

        # tabs
        self.add("Position")
        self.add("Colour")
        self.add("Effects")
        self.add("Export")

        # create widgets
        PositionFrame(self.tab("Position"))
        ColourFrame(self.tab("Colour"))

class PositionFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color="transparent")
        self.pack(expand=True, fill="both")
        
        SliderPanel(self, "Hi")
        
class ColourFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color="transparent")
        self.pack(expand=True, fill="both")