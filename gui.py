#import libraries
import tkinter
from tkinter import *
from tkinter import filedialog

#Initializing the root box
root = Tk()
root.title('Image to Text Converter') #Header
root.geometry('750x500') #Size of the Window
root.resizable(False,False)

#-----Initializing the new Label-----#
BLANK_LABEL = Label(root, text="  ").grid(row=0, column=0 )
##TEXT
applicationTitle = Label(root, text="DigiDocs", font=('Times', 24))
applicationSubHeading = Label(root, text="Image to Document Analyzer", font=('tahoma', 15) )
DIRECTORY_DEBUG = Text(
        root,
        height=3,
        width=25,
        state = NORMAL
    )
##FUNCTIONS
def openFile():
    root.filename = filedialog.askopenfilename(initialdir="./sample",
                                               title="Open Image",
                                               filetypes=(
                                                   ("png files","*.png"),
                                                   ("jpeg files", "*.jpeg"),
                                                   ("all files", "*.*")
                                               )
                                               )

    DIRECTORY_DEBUG.insert(tkinter.END, root.filename)

##BUTTONS
uploadFileButton = Button(root,
                          text="Upload Photos",
                          command=openFile,
                          height=5,
                          width=15
                          )
#----Putting the Label in GUI------#
##TEXT
applicationTitle.grid(row = 1, column = 0, padx = 3, pady = 2)
applicationSubHeading.grid(row = 2, column = 0, padx= 3, pady= 2)
DIRECTORY_DEBUG.grid(row=4, column=0)


##BUTTONS
uploadFileButton.grid(row = 3, column = 1, padx = 50, pady = 0)

#Initializing the main
root.mainloop()