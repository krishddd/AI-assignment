import numpy as np
import cv2
import os

image_path = input("Enter a fully qualified path for an image: ")
#define a function to load an image
def img_loader(img_path):
    exists = os.path.isfile(img_path)
    if exists:
        img = cv2.imread(img_path)
        print("Success! The image path exists")
        return img
    else:
        print("WARNING: The file path you entered was incorrect.")
        return None

load=img_loader(image_path)   
print(load)