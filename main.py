import pytesseract as pt
import os
import cv2
from PIL import Image

def showImage(image_path):
    image = cv2.imread(image_path)
    cv2.imshow("YOUR INPUT", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def testCode_listAllImageFiles():
    for f in image_files:
        print(f)

test_img_path = "test images"
create_path = lambda f: os.path.join(test_img_path, f)

image_files = os.listdir(test_img_path)

image_path = image_files[2]
path = create_path(image_path)

image = Image.open(path)
text = pt.image_to_string(image)

print(text)
showImage(path)