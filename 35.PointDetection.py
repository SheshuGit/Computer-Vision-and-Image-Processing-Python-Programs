import cv2

# Load the image
image = cv2.imread('sample.jpg', cv2.IMREAD_GRAYSCALE)

# Apply Laplacian operator
laplacian = cv2.Laplacian(image, cv2.CV_64F)

# Calculate the absolute value of the Laplacian
laplacian_abs = cv2.convertScaleAbs(laplacian)

# Threshold the Laplacian image to identify points
_, points = cv2.threshold(laplacian_abs, 30, 255, cv2.THRESH_BINARY)

# Display the original image and the detected points
cv2.imshow('Original Image', image)
cv2.imshow('Detected Points', points)
cv2.waitKey(0)
cv2.destroyAllWindows()
