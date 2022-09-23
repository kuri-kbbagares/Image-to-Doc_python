import pytesseract as pt
import os
import cv2
from PIL import Image

##SETUP

test_img_path = "test images" #StringVar of path where the pictures are located
create_path = lambda f: os.path.join(test_img_path, f) #Processes the PATH to join with the existing path (Existing path: .../Image-to-Doc_python)

image_files = os.listdir(test_img_path) #Create an index of all the files in the directory
image_path = image_files[0] #Var that holds the path of an image in an index image_files

path = create_path(image_path) #Var that holds the created path

def showImage(image_path):
    image = cv2.imread(image_path)
    cv2.imshow("YOUR INPUT", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def process():
    custom_oem_psm_config = ''

    image = Image.open(path)
    text = pt.image_to_string(image, config='--psm 13')

    try:
        x = text[0]
    except IndexError:
        print("Failed to recognize text")
        return 0
    else:
        print("Here is the text: \n", text)
    showImage(path)

def insert_image():
    exit() #temp-code

def delete_image(path):
    os.remove(path)
    menu()

def menu():
    print("\n")
    print("|-------------------------|")
    print("| Image to Text Converter |")
    print("|-------------------------|")

    print("1. Run the program")
    print("2. Insert Image (WIP)")
    print("3. Remove Image (WIP)")
    print("4. Exit")
    userInput = input("What will be your option:")
    if userInput == "1":
        process()
    elif userInput == "3":
        delete_image(path)
    elif userInput == "4":
        exit()
    else:
        menu()
##LOOP
menu()