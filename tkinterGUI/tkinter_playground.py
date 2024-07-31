import tkinter as tk

# create a window
window = tk.Tk()
window.title("playground")
window.geometry("200x400")

# widgets
text = tk.Text(master=window)
text.pack()

# run
window.mainloop()
print("I was blocked by the mainloop until now")

# --------------------------------------------- #
#                 tutorial end                  #
#        checking required elements             #
# --------------------------------------------- #