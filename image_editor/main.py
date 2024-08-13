import customtkinter as ctk
from PIL import Image, ImageTk, ImageOps, ImageEnhance
from image_widgets import *
from menu import Menu

class App(ctk.CTk):
    def __init__(self):
        # setup
        super().__init__()
        ctk.set_appearance_mode("dark")
        self.geometry("1000x600")
        self.title("Photo Editor")
        self.minsize(800,500)
        
        self.init_parameters()

        # layout    
        self.rowconfigure(0, weight=1)
        # TODO: WIT "uniform"
        self.columnconfigure(0, weight=2, uniform="a")
        self.columnconfigure(1, weight=6, uniform="a")

        # canvas data init
        self.image_width = 0
        self.image_height = 0
        self.canvas_width = 0
        self.canvas_height = 0

        # widgets
        # ImportButton (Frame with a button), TODO: why?
        self.image_import = ImageImport(self, self.import_image)

        # run
        self.mainloop()

    def init_parameters(self):
        self.pos_vars = {
            "rotate": ctk.DoubleVar(value=ROTATE_DEFAULT),
            "zoom": ctk.DoubleVar(value=ZOOM_DEFAULT),
            "flip": ctk.StringVar(value=FLIP_OPTIONS[0])
        }
        self.colour_vars = {
            "brightness": ctk.DoubleVar(value=BRIGHTNESS_DEFAULT),
            "greyscale": ctk.BooleanVar(value=GREYSCALE_DEFAULT),
            "invert": ctk.BooleanVar(value=INVERT_DEFAULT),
            "vibrance": ctk.DoubleVar(value=VIBRANCE_DEFAULT)
        }
        self.effect_vars = {
            "blur": ctk.DoubleVar(value=BLUR_DEFAULT),
            "contrast": ctk.IntVar(value=CONTRAST_DEFAULT),
            "effect": ctk.StringVar(value=EFFECT_OPTIONS[0])
        }
        combined_vars = list(self.pos_vars.values()) + list(self.colour_vars.values()) + list(self.effect_vars.values())

        # trace changes to the var << ?
        for var in combined_vars:
            var.trace("w", self.manipulate_image)

    def manipulate_image(self, *args):  # TODO: WIT '*args'
        self.image = self.original

        # rotate (# use the var value to change the image << bind/trace..?)
        self.image = self.image.rotate(self.pos_vars["rotate"].get())

        # zoom (this is the simplest zoom option in PIL, but does stretch images a bit)
        self.image = ImageOps.crop(image=self.image, border=self.pos_vars["zoom"].get())

        # flip
        if self.pos_vars["flip"].get() == "X":
            self.image = ImageOps.mirror(self.image)
        if self.pos_vars["flip"].get() == "Y":
            self.image = ImageOps.flip(self.image)
        if self.pos_vars["flip"].get() == "Both":
            self.image = ImageOps.mirror(self.image)
            self.image = ImageOps.flip(self.image)

        # brightness & vibrance
        brightness_enhancer = ImageEnhance.Brightness(self.image)
        self.image = brightness_enhancer.enhance(self.colour_vars["brightness"].get())
        vibrance_enhancer = ImageEnhance.Color(self.image)
        self.image = vibrance_enhancer.enhance(self.colour_vars["vibrance"].get())

        self.place_image()

    def import_image(self, path):
        print(path)  # DEBUG
        # TODO: case when dialog opened but no image selected, AttributeError
        self.original = Image.open(path)
        self.image = self.original
        self.image_ratio = self.image.size[0] / self.image.size[1]
        self.image_tk = ImageTk.PhotoImage(self.image)

        # DEBUG, display with Python
        # self.image.show()
        # display within tkinter
        # hide the image import widget
        self.image_import.grid_forget()
        self.image_output = ImageOutput(self, self.resize_image)

        # s.ab.(+WIT) rather than passing in the image into ImageOutput, 
        #  we want to keep the image within the App class (s.ab. logic staying contained)

        self.close_button = CloseOutput(self, self.close_edit)
        # connect the var to the slider << pass the value on and on
        self.menu = Menu(self, self.pos_vars, self.colour_vars, self.effect_vars)
    
    def close_edit(self):
        # hide image and close button
        # TODO: which forgets to use!!
        self.image_output.grid_forget()
        self.close_button.place_forget()
        self.menu.grid_forget()

        # recreate the import button
        self.image_import = ImageImport(self, self.import_image)

    def resize_image(self, event):
        """
        takes the canvas width:height ratio to then fit the image within the canvas, 
        preserving the image ratio but not cutting off the edges.
        """
        # print(event)  # DEBUG

        canvas_ratio = event.width / event.height

        # update canvas attributes
        self.canvas_width = event.width
        self.canvas_height = event.height

        # and image ratio
        if canvas_ratio > self.image_ratio:  # image should fit in hor
            self.image_height = int(event.height)
            self.image_width = int(self.image_height * self.image_ratio)
        else:  # image does not fit in hor
            self.image_width = int(event.width)
            self.image_height = int(self.image_width / self.image_ratio)

        self.place_image()

    def place_image(self):
        # placing the image
        # need to remove the previous image
        self.image_output.delete("all")
        resized_image = self.image.resize((self.image_width, self.image_height))
        self.image_tk = ImageTk.PhotoImage(resized_image)

        # print(event)
        # seems to be centering the image (not top-left like Pygame)
        self.image_output.create_image(self.canvas_width/2, self.canvas_height/2, image=self.image_tk)

App()