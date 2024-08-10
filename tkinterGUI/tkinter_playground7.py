import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.title("playground 7 - combobox and spinbox")
window.geometry("500x500")

# combobox
items = ("Ice cream", "Pizza", "Broccoli")
food_string = tk.StringVar(value=items[0])
combo = ttk.Combobox(window, textvariable=food_string)
combo["values"] = items  # recommended
# combo.configure(values=items)
combo.pack()

# events
# option 1
# combo.bind("<<ComboboxSelected>>", lambda event: print(food_string.get()))
# combo_label = ttk.Label(window, textvariable=food_string)
# option 2
combo.bind("<<ComboboxSelected>>", lambda event: combo_label.config(text=f"Selected value: {food_string.get()}"))
combo_label = ttk.Label(window, text="a label")
combo_label.pack()

# spinbox
# Watch out for inconsistency with increments
spin_int = tk.IntVar(value=12)
spin = ttk.Spinbox(
        window, 
        from_=3,
        to=20, 
        increment=3, 
        command=lambda: print("spinbox at: " + str(spin_int.get())),
        textvariable=spin_int)
spin.bind("<<Increment>>", lambda event: print("up"))
spin.bind("<<Decrement>>", lambda event: print("down"))
# spin["value"] = (1,2,3,4,5)
spin.pack()

exercise_letters = ("A", "B", "C", "D", "E")
my_spin_string = tk.StringVar(value=exercise_letters[0])
my_spinbox = ttk.Spinbox(
        window,
        values=exercise_letters,
        textvariable=my_spin_string
)
my_spinbox.bind("<<Decrement>>", lambda event: print("Value: ", my_spin_string.get()))
my_spinbox.pack()

# run
window.mainloop()