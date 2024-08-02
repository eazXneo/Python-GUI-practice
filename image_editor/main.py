import customtkinter as ctk
from PIL import Image, ImageTk
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

        # layout
        self.rowconfigure(0, weight=1)
        # TODO: WIT "uniform"
        self.columnconfigure(0, weight=2, uniform="a")
        self.columnconfigure(1, weight=6, uniform="a")

        # widgets
        # ImportButton (Frame with a button), TODO: why?
        self.image_import = ImageImport(self, self.import_image)

        # run
        self.mainloop()

    def import_image(self, path):
        print(path)  # DEBUG
        # TODO: case when dialog opened but no image selected, AttributeError
        self.image = Image.open(path)
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

        # self.resize_image()

        self.close_button = CloseOutput(self, self.close_edit)
        self.menu = Menu(self)
    
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
        # need the aspect ratio of image
        #  and canvas
        canvas_ratio = event.width / event.height
        if canvas_ratio > self.image_ratio:  # image should fit in hor
            image_height = int(event.height)
            image_width = int(image_height * self.image_ratio)
        else:  # image does not fit in hor
            image_width = int(event.width)
            image_height = int(image_width / self.image_ratio)

        # placing the image
        # need to remove the previous image
        self.image_output.delete("all")
        resized_image = self.image.resize((image_width, image_height))
        self.image_tk = ImageTk.PhotoImage(resized_image)

        # print(event)
        # seems to be centering the image (not top-left like Pygame)
        self.image_output.create_image(event.width/2, event.height/2, image=self.image_tk)

App()