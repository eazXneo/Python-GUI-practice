import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.title("playground 4 - buttons")
window.geometry("300x200")

# button
def button_func():
    print("A basic button function")
    print("Radio status:", radio_var.get())

button_string_var = tk.StringVar(value="a button with string var")
# button = ttk.Button(window, text="simple button", command=lambda: print("a button basic press (by lambda)"))
button = ttk.Button(window, text="simple button", command=button_func, textvariable=button_string_var)
button.pack()

# checkbutton - starts with the neutral checkbox value [-]
#  but starts with [ ] if variable connected (TODO: WIT)
#  can have more complicated logic, but watch out if you just want the checkboxes to behave normally
check_var = tk.IntVar(value=10)  # set the start to [X] (checked)
check1 = ttk.Checkbutton(
        window, 
        text="checkbox 1", 
        command=lambda: print(check_var.get()),
        variable=check_var,  # not a textvariable, because this is the value not the text displayed...?
        onvalue=10,
        offvalue=5)
check1.pack()
check2 = ttk.Checkbutton(
        window,
        text="Checkbox 2",
        command=lambda: check_var.set(5))
check2.pack()

# radio buttons, the widgets need a unique value to not trigger unwanted side effects..!
radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(
        window, 
        text="Radiobutton 1", 
        value="radio 1", 
        command=lambda: print(radio_var.get()),
        variable=radio_var)
radio1.pack()
radio2 = ttk.Radiobutton(
        window, 
        text="Radiobutton 2", 
        value=2,
        command=lambda: print(radio_var.get()),
        variable=radio_var)
radio2.pack()

def radio_func():
    print("Checkbutton status:", check3_var.get())
    check3_var.set(False)

# data
ex_radio_var = tk.StringVar()
check3_var = tk.BooleanVar()

# widgets
radio3 = ttk.Radiobutton(
        window,
        text="Exercise radio button A",
        value="A",
        command=radio_func,
        variable=ex_radio_var)
radio4 = ttk.Radiobutton(
        window,
        text="Exercise radio button B",
        value="B",
        command=radio_func,  
        variable=ex_radio_var)
check3 = ttk.Checkbutton(
        window,
        text="Exercise checkbox",
        variable=check3_var,
        command=lambda: print("Radio button val: ", ex_radio_var.get()) if check3_var.get()==True else 3+3)

# layout
radio3.pack()
radio4.pack()
check3.pack()

window.mainloop()