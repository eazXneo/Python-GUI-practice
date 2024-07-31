import customtkinter as ctk
from image_widgets import ImageImport, ImageOutput
from PIL import Image, ImageTk

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
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=6)

        # widgets
        # ImportButton (Frame with a button), TODO: why?
        self.image_import = ImageImport(self, self.import_image)

        # run
        self.mainloop()

    def import_image(self, path):
        print(path)  # DEBUG
        # TODO: case when dialog opened but no image selected, AttributeError
        self.image = Image.open(path)
        self.image_tk = ImageTk.PhotoImage(self.image)

        # DEBUG, display with Python
        # self.image.show()  
        # display within tkinter
        # hide the image import widget
        self.image_import.grid_forget()
        self.image_output = ImageOutput(self)

        # s.ab.(+WIT) rather than passing in the image into ImageOutput, 
        #  we want to keep the image within the App class (s.ab. logic staying contained)

        self.resize_image()

    def resize_image(self):
        self.image_output.create_image(0, 0, image=self.image_tk)

App()