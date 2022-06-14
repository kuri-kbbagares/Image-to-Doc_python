import pytesseract
import os
import cv2
from PIL import Image

test_img_path = "test images"
create_path = lambda f: os.path.join(test_img_path, f)

test_image_files = os.listdir(test_img_path)

for f in test_image_files:
    print(f)


