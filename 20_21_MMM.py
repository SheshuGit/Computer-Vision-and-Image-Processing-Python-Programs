import cv2
import numpy as np

# Load the image
image = cv2.imread('charlie.png', 0)  # 0 for grayscale



# 2. Minimum Filter
kernel = np.ones((5, 5), np.uint8)
minimum = cv2.erode(image, kernel, iterations=1)  # Apply minimum filter
cv2.imshow('Minimum Filter', minimum)

# 3. Maximum Filter
kernel = np.ones((5, 5), np.uint8)
maximum = cv2.dilate(image, kernel, iterations=1)  # Apply maximum filter
cv2.imshow('Maximum Filter', maximum)

cv2.waitKey(0)
cv2.destroyAllWindows()