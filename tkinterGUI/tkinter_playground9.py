import tkinter as tk
from tkinter import ttk
from random import choice

# setup
window = tk.Tk()
window.title("playground 9 - treeview")
window.geometry("600x400")

# data
first_names = ["Bob", "Maria", "Alex", "James", "Susan", "Henry", "Lisa", "Anna", "Lisa"]
last_names = ["Smith", "Brown", "Wilson", "Thomson", "Cook", "Taylor", "Walker", "Clark"]

# treeview
table = ttk.Treeview(window, columns=("first", "last", "email"), show="headings")
table.heading("first", text="First name")
table.heading("last", text="Surname")
table.heading("email", text="Email")
table.pack(fill="both", expand=True)

# insert values into a table
# table.insert(parent="", index=0, values=("John", "Doe", "JohnDoe@email.com"))
for i in range(100):
    random_first = choice(first_names)
    random_last = choice(last_names)
    # generated_email = random_first + random_last + "@email.com"
    generated_email = f"{random_first[0]}{random_last}@email.com"
    data = (random_first, random_last, generated_email)
    # table.insert(parent="", index=i, values=(random_first, random_last, generated_email))
    table.insert(parent="", index=i, values=data)

table.insert(parent="", index=tk.END, values=("XXXXX", "YYYYY", "ZZZZZ"))

# events and items
def item_select(_):
    print(table.selection())
    # table.item(table.selection()[0])
    for i in table.selection():
        print(table.item(i)["values"])

def delete_items(_):
    print("To be deleted: ", table.selection())
    # # delete the actual entry
    # table.delete(item_to_delete)

    # handling multiple things selected ...
    for i in table.selection():
        table.delete(i)

# table.bind("<<TreeviewSelect>>", lambda event: print(table.selection()))
table.bind("<<TreeviewSelect>>", item_select)
table.bind("<BackSpace>", delete_items)

# run
window.mainloop()