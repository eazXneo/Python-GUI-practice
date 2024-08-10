import customtkinter as ctk
from settings import *

class Panel(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color=DARK_GREY)
        self.pack(fill="x", pady=4, ipady=8)

class SliderPanel(Panel):
    def __init__(self, parent, text, data_var, min_value, max_value):
        super().__init__(parent=parent)

        # layout
        # self.rowconfigure(0, weight=1)
        # self.rowconfigure(1, weight=1)
        self.rowconfigure((0,1), weight=1)  # simpler way of saying the above
        # self.columnconfigure(0, weight=1)
        # self.columnconfigure(1, weight=1)
        self.columnconfigure((0,1), weight=1)  # simpler way of saying the above
        
        ctk.CTkLabel(self, text=text).grid(column=0, row=0, sticky="w", padx=5)
        # TODO: round about way to round value to then display in label
        self.num_label = ctk.CTkLabel(self, text=data_var.get())
        self.num_label.grid(column=1, row=0, sticky="e", padx=5)
        ctk.CTkSlider(
                self, 
                fg_color=SLIDER_BG, 
                variable=data_var,
                from_=min_value,
                to=max_value,
                command=self.update_text
                ).grid(column=0, row=1, columnspan=2, sticky="we", padx=5, pady=5)

        # my try...
        # name_label = ctk.CTkLabel(self, text=text)
        # name_label.grid(column=0, row=0, sticky="w", padx=5, pady=5)

        # slider_val_label = ctk.CTkLabel(self, text="0.0")
        # slider_val_label.grid(column=0, row=0, sticky="e", padx=5, pady=5)

        # slider_pl = ctk.CTkLabel(self, text="imagine a slider here...")
        # slider_pl.grid(column=0, row=1, sticky="we", padx=5, pady=5)

    def update_text(self, value):
        self.num_label.configure(text=f"{round(value, 2)}")

class SegmentedPanel(Panel):
    def __init__(self, parent, text, data_var, options):
        super().__init__(parent=parent)
        ctk.CTkLabel(self, text=text).pack()
        ctk.CTkSegmentedButton(self, variable=data_var, values=options).pack(expand=True, fill="both", padx=4, pady=4)

class SwitchPanel(Panel):
    def __init__(self, parent, *args):  # tuple of tuples ((var, text), ... , (var, text))
        super().__init__(parent=parent)

        for var, text in args:
            pass  # TODO