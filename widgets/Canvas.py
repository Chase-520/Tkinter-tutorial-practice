import tkinter as tk

"""
We will learn about basic method for canvas widget in tk and understanding canvas hierarchy
"""

# craete a tk window
root = tk.Tk() # this create a root windwo for all tk widgets

# create a tk canvas
"""
Canvas("parent window/widget", "width", "height")
"""
canvas = tk.Canvas(root, width=800, height=600)


# loop the window, keep the window showing
root.mainloop()