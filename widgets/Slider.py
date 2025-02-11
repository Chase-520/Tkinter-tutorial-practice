from tkinter import *

root = Tk()
root.geometry("800x600")

# create a frame to hold both canvas and scroll bar
frame = Frame(root)

# display frame
frame.pack()

# set up a canvas
canvas = Canvas(master=frame,width=800,height=500,bg="lightgrey")

# display canvas
canvas.pack()

# create a slider using scale object
slide = Scale(master=frame,orient=HORIZONTAL)

# display slider
slide.pack(fill="both")


root.mainloop()