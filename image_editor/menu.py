import customtkinter as ctk
from panels import *

class Menu(ctk.CTkTabview):  # a frame with tabs
    def __init__(self, parent, pos_vars, colour_vars, effect_vars):
        super().__init__(master=parent)
        self.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # tabs
        self.add("Position")
        self.add("Colour")
        self.add("Effects")
        self.add("Export")

        # create widgets
        PositionFrame(self.tab("Position"), pos_vars)
        ColourFrame(self.tab("Colour"), colour_vars)
        EffectFrame(self.tab("Effects"), effect_vars)

class PositionFrame(ctk.CTkFrame):
    def __init__(self, parent, pos_vars):
        super().__init__(master=parent, fg_color="transparent")
        self.pack(expand=True, fill="both")
        
        SliderPanel(self, "Rotation", pos_vars["rotate"], 0, 360)
        SliderPanel(self, "Zoom", pos_vars["zoom"], 0, 200)
        SegmentedPanel(self, "Invert", pos_vars["flip"], FLIP_OPTIONS)

        
class ColourFrame(ctk.CTkFrame):
    def __init__(self, parent, colour_vars):
        super().__init__(master=parent, fg_color="transparent")
        self.pack(expand=True, fill="both")

        SwitchPanel(self, (colour_vars["greyscale"], "B/W"), (colour_vars["invert"], "Invert"))
        SliderPanel(self, "Brightness", colour_vars["brightness"], 0, 5)
        SliderPanel(self, "Vibrance", colour_vars["vibrance"], 0, 5)

class EffectFrame(ctk.CTkFrame):
    def __init__(self, parent, effect_vars):
        super().__init__(master=parent, fg_color="transparent")
        self.pack(expand=True, fill="both")

        DropDownPanel(self, effect_vars["effect"], EFFECT_OPTIONS)
        SliderPanel(self, "Blur", effect_vars["blur"], 0, 3)
        SliderPanel(self, "Contrast", effect_vars["contrast"], 0, 10)