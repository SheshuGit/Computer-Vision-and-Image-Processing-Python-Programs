import numpy as np
import cv2
import matplotlib.pyplot as plt

# Load the input image
image = cv2.imread('download.jpg', cv2.IMREAD_GRAYSCALE)

kernel_h = np.array([1, 0, -1])  
kernel_v = np.array([[-1], [0], [1]])  

correlated_h = cv2.filter2D(image, -1, kernel_h)

correlated_V = cv2.filter2D(image, -1, kernel_v, )

# Display the original and correlated images
plt.figure(figsize=(12, 6))

plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

plt.subplot(2, 2, 2)
plt.imshow(correlated_h, cmap='gray')
plt.title('Horizontal Correlation')

plt.subplot(2, 2, 3)
plt.imshow(correlated_V, cmap='gray')
plt.title('Vertical Correlation')

plt.tight_layout()
plt.show()
