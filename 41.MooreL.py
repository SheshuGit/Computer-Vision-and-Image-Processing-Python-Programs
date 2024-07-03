import cv2
import numpy as np

# Load the image
chirag = cv2.imread('apple.png')

# Convert the image to grayscale
gray_img = cv2.cvtColor(chirag, cv2.COLOR_BGR2GRAY)

# Threshold the grayscale image
_, img = cv2.threshold(gray_img, 225, 255, cv2.THRESH_BINARY_INV)

# Apply median blur to reduce noise
img = cv2.medianBlur(img, 3)

# Find contours
contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours on the original image
contour_img = cv2.drawContours(chirag.copy(), contours, -1, (0, 255, 0), 2)

# Display the contour image
cv2.imshow('Contours', contour_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
