import cv2

# Load the input image
img = cv2.imread('download.jpg')

# Define the scaling factor
scale_factor = 1.2

# Apply scaling
scaled_img = cv2.resize(img, None, fx=scale_factor, fy=scale_factor)

# Display original and scaled images
cv2.imshow('Original Image', img)
cv2.imshow('Scaled Image', scaled_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


import cv2
import numpy as np

# Load the input image
img = cv2.imread('download.jpg')

# Define scaling factor
scale_factor = 1.2

# Define scaling matrix
M = np.array([[scale_factor, 0, 0],
              [0, scale_factor, 0]], dtype=np.float32)

# Apply affine transformation
scaled_img = cv2.warpAffine(img, M, (int(img.shape[1]*scale_factor), int(img.shape[0]*scale_factor)))

# Display original and scaled images
cv2.imshow('Original Image', img)
cv2.imshow('Scaled Image', scaled_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
