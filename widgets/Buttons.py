from tkinter import *

"""
Introduction for buttons in tkinter
"""

# create a root window
root = Tk()
root.geometry("800x600")
# create a canvas
canvas = Canvas(master=root,width=720,height=360,bg="lightgrey")

# display canvas
canvas.pack()

# create a button
button1 = Button(master=canvas,text="Button")

# display button1
button1.pack()

"""
Radio button is different then a normal button,
In a set of radio button, uesr can only select one 
"""

# create a tk string object to store all tk string
v = StringVar(root, "1")

# create a radio button
button2 = Radiobutton(master=canvas,text="radio1",variable=v,value=1)
button3 = Radiobutton(master=canvas,text="radio2",variable=v,value=2)

# display radio buttons
button2.pack()
button3.pack()

# loop the window
root.mainloop()