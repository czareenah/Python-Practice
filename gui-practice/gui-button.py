from tkinter import *

 # Root widget - the main window 
root = Tk()
# GUI Requirement 1: Define - Creating a label widget 
    # myLabel = Label(root, text="Hello World!")

# To get a button to do something, you create a function
def myClick():
    myLabel = Label(root, text="I'm not touching you!", fg="white", bg="red")
    myLabel.pack()

myButton = Button(root, text="She's touching me!", command=myClick, fg="white", bg="blue")
# You can change the button's stages. To disable, add state=DISABLED
# Changing sizes is easy with adding padx=(), pady=()
# To execute the function of the button, add:  command=Function 
# To add colour to text:  fg="colour" | To add button colour (background): bg="colour"
# You can also use HEX colour codes ="#-----"

# GUI Requirement 2: Pack - Shoving the label into the screen
myButton.pack()

# Creating a loop! Loops only gets disrupted when the window has been closed
root.mainloop()