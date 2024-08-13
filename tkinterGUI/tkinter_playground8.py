import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.title("playground 8 - canvas")
window.geometry("600x400")

# canvas
canvas = tk.Canvas(window, bg="dark green")
canvas.pack()

# TODO: WIT, dash on Mac not working...?
# canvas.create_rectangle((50, 20, 100, 200), fill="blue", width=5, dash=(4,2,1,1), outline="yellow")
# canvas.create_oval((150, 0, 250, 100), fill="green")
# canvas.create_arc(
#         (150, 0, 250, 100), 
#         fill="red", 
#         start=45, 
#         extent=140, 
#         style=tk.CHORD, 
#         outline="red", 
#         width=1)

# canvas.create_line((0, 0, 100, 150), fill="red")
# canvas.create_polygon((0,0, 100,200, 300,50, 150,-50), fill="white")

# canvas.create_text((90,100), text="some sort of text.", fill="crimson", width=10)

# canvas.create_window((100,200), window=ttk.Label(window, text="text in label on canvas. no need to pack"))
# canvas.create_window((100,200), window=ttk.Button(window, text="button on canvas. no need to pack"))

# my try
# last_pos = None

# def mouse_moved(event, last_pos):
#     print(event)
#     print(last_pos)
#     if last_pos is None:
#         last_pos = (event.x, event.y)
#     else:
#         canvas.create_line((last_pos[0], last_pos[1], event.x, event.y))
#         last_pos = (event.x, event.y)

# canvas.bind('<Motion>', (lambda event: mouse_moved(event, last_pos)))

# remember the scope of variables: https://realpython.com/python-use-global-variable-in-function/ 

def draw_on_canvas(event):
    x = event.x
    y = event.y
    # ! smart idea to use an oval (circle) AROUND the mouse.
    canvas.create_oval((x - (brush_size / 2), y - (brush_size / 2), x + (brush_size / 2), y + (brush_size / 2)), fill="white")

def brush_size_adjust(event):
    global brush_size
    if event.delta > 0:
        brush_size += 4
        # brush_size = brush_size + 4 if brush_size < 27 else brush_size
    else:
        brush_size -= 4
        # brush_size = brush_size - 4 if brush_size > 4 else brush_size

    brush_size = max(0, min(brush_size, 40))

    print(event)

brush_size = 2
canvas.bind('<Motion>', draw_on_canvas)
canvas.bind("<MouseWheel>", brush_size_adjust)

# run
window.mainloop()