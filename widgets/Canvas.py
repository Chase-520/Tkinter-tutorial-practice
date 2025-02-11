from tkinter import *

"""
We will learn about basic method for canvas widget in tk and understanding canvas hierarchy
"""

# craete a tk window
root = Tk() # this create a root windwo for all tk widgets
root.geometry("800x600") # set window size

# create a tk canvas
"""
Canvas("parent window/widget", "width", "height")
"""
canvas = Canvas(master=root, width=800, height=600 ,bg="red")

# draw somehing in the canvas
canvas.create_rectangle(50,50,500,300,fill="blue")

"""
now lets' try to create a canvas inside the previous canvas
"""
# create a canvas object
canva = Canvas(master=canvas,width=400,height=300,bg="black")

# display canva using create_window from master canvas object
canvas.create_window(400, 400, window=canva)

# show all canvas by calling pack()
canvas.pack()

# loop the window, keep the window showing
root.mainloop()