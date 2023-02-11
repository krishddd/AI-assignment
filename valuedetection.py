import cv2
import numpy as np

# Load the image
image = cv2.imread('coins.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Use Otsu's thresholding to binarize the image
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Find the contours in the binarized image
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw the contours on the original image
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

# Print the number of contours (which correspond to the number of coins in the image)
print("Number of coins: ", len(contours))

# Show the image with the contours drawn on it
cv2.imshow("Coins", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
