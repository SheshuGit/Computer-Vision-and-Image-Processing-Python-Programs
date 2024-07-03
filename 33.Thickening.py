import cv2
import numpy as np

# Create an image with text
img = np.zeros((100, 400), dtype='uint8')
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'SHESHU', (5, 70), font, 2, (255), 5, cv2.LINE_AA)
img1 = img.copy()

# Define the structuring element
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
thick = np.zeros(img.shape, dtype='uint8')

# Perform thickening
while cv2.countNonZero(img1) != 0:
    dilate = cv2.dilate(img1, kernel)
    closing = cv2.morphologyEx(dilate,cv2.MORPH_CLOSE,kernel)
    subset = dilate - closing  # Find the pixels that changed after dilation
    thick = cv2.bitwise_or(subset, thick)
    img1 = dilate.copy()

# Display the original and thickened images
cv2.imshow('Original', img)
cv2.imshow('Thickened', thick)
cv2.waitKey(0)
cv2.destroyAllWindows()
