# Requirement: Positioning and grid system (rows, col)
from tkinter import *

 # Root widget - the main window 
root = Tk()

# Define - Creating a label widget 
myLabel1 = Label(root, text="Hello World!").grid(row=0, column=0)
myLabel2 = Label(root, text="Goodbye World!").grid(row=1, column=2)
myLabel3 = Label(root, text="I'll be back...").grid(row=2, column=3)

# Grid - Shoving the label into the screen (.grid(where we want things)) 
# Note: Code is relative to each other
# Long way example: 
#     myLabel1.grid(row=0, column=0)
#     myLabel2.grid(row=1, column=2) 
#     myLabel3.grid(row=2, column=3)

# Creating a loop 
root.mainloop()

# Positioning and grid system (rows, col)
