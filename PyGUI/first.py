# this is the folder that has all the GUI using Python
# for this, we will be using Tkinter

# widgets => GUI Elements
# window => container-that dialog box

from tkinter import *
window=Tk()                         # creates a window instance

window.geometry("500x500")
window.title("FIRST GUI")           # changes the top window title

# to change the icon, we do this:-
# icon=PhotoImage(file=<filePath>)
# window.iconphoto(True, icon)

window.config(background="black")   # adding the background on the window
window.mainloop()                   # place window on screen