import cv2
import numpy as np

# Load the input image
img = cv2.imread('download.jpg')

# Define skew angles
skew_angle_x = 20  # Skew angle along x-axis (in degrees)
skew_angle_y = 10  # Skew angle along y-axis (in degrees)

# Get the height and width of the input image
rows, cols, _ = img.shape

# Calculate the skew transformation matrices
M_x = np.float32([[1, np.tan(np.deg2rad(skew_angle_x)), 0],
                  [0, 1, 0]])

M_y = np.float32([[1, 0, 0],
                  [np.tan(np.deg2rad(skew_angle_y)), 1, 0]])

# Apply skew transformations
skewed_img_x = cv2.warpAffine(img, M_x, (cols, rows))
skewed_img_y = cv2.warpAffine(img, M_y, (cols, rows))

# Display the original and skewed images
cv2.imshow('Original Image', img)
cv2.imshow('Skewed Image along x-axis', skewed_img_x)
cv2.imshow('Skewed Image along y-axis', skewed_img_y)
cv2.waitKey(0)
cv2.destroyAllWindows()
