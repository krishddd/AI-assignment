import cv2
import pytesseract
from PIL import Image

img = cv2.imread('C:\Users\hp\OneDrive\Documents\IT Automation', cv2.IMREAD_GRAYSCALE)

thresh = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)[1]

print(pytesseract.image_to_string(img, config='--psm 6'))