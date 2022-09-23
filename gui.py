#import libraries
from tkinter import *
from tkinter import filedialog

#Initializing the root box
root = Tk()
root.title('Image to Text Converter') #Header
root.geometry('500x250')
root

#-----Initializing the new Label-----#
BLANK_LABEL = Label(root, text = "  ").grid(row = 0, column = 0 )
##TEXT
applicationTitle = Label(root, text="DigiDocs", font=('Times', 24))
applicationSubHeading = Label(root, text="Image to Document Analyzer", font=('tahoma', 15) )

##BUTTONS
uploadFileButton = Button(root, text = "Upload Photos")


#----Putting the Label in GUI------#
##TEXT
applicationTitle.grid(row = 1, column = 0, padx = 3, pady = 2)
applicationSubHeading.grid(row = 2, column = 0, padx= 3, pady= 2)

##BUTTONS
uploadFileButton.grid(row = 2, column = 1, padx = 50, pady = 2)

#Initializing the main
root.mainloop()