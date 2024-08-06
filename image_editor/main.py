import customtkinter as ctk
from PIL import Image, ImageTk, ImageOps
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
        self.rotate_float = ctk.DoubleVar(value=ROTATE_DEFAULT)
        self.zoom_float = ctk.DoubleVar(value=ZOOM_DEFAULT)

        # trace changes to the var << ?
        self.rotate_float.trace("w", self.manipulate_image)  # TODO: WIT trace
        self.zoom_float.trace("w", self.manipulate_image)

    def manipulate_image(self, *args):  # TODO: WIT '*args'
        self.image = self.original

        # rotate (# use the var value to change the image << bind/trace..?)
        self.image = self.image.rotate(self.rotate_float.get())

        # zoom (this is the simplest zoom option in PIL, but does stretch images a bit)
        self.image = ImageOps.crop(image=self.image, border=self.zoom_float.get())

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
        self.menu = Menu(self, self.rotate_float, self.zoom_float)
    
    def close_edit(self):
        # hide image and close button
        # TODO: which forgets to use!!
        self.image_output.grid_forget()
        self.close_button.place_forget()
        self.menu.grid_forget()

        # recreate the import button
        self.image_import = ImageImport(self, self.import_image)

    def resize_image(self, event):
        # resize image (don't want to cut parts off the image when resizing window)
        # need the aspect ratio of canvas
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