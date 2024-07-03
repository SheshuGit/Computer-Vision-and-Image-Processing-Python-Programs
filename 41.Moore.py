import cv2
import numpy as np

# Load the image
chirag = cv2.imread('shapes.png')

# Convert the image to grayscale
gray_img = cv2.cvtColor(chirag, cv2.COLOR_BGR2GRAY)

# Threshold the image to get a binary image
_, img = cv2.threshold(gray_img, 225, 255, cv2.THRESH_BINARY_INV)

# Apply median blur to reduce noise
img = cv2.medianBlur(img, 3)

# Initialize starting pixel and contour list
starting_pixel = np.transpose(np.where(img == 255))
B = [tuple(starting_pixel[0])]  # Convert starting pixel to tuple and add to contour list

# Define offset table for Moore-Neighbor algorithm
offsetTable = [(0, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

# Initialize variables for direction vector
prev_x, prev_y = B[0]

# Initialize count of traced contour segments
count = 1

# Initialize contour image
contour = np.zeros(chirag.shape, dtype=np.uint8)

# Main loop for contour tracing
while count <= 2:
    for offset in offsetTable:
        c_x, c_y = prev_x + offset[0], prev_y + offset[1]
        if img[c_x, c_y] != 0:
            B.append((c_x, c_y))
            contour[c_x, c_y] = [0, 255, 0]  # Mark contour pixel as green
            count += 1
            if count % 100 == 0:
                cv2.imshow('Image_contour', contour)
                cv2.waitKey(0)
            prev_x, prev_y = c_x, c_y
            break

# Show the final contour image
cv2.imshow('Image_contour', contour)
cv2.waitKey(0)
cv2.destroyAllWindows()
