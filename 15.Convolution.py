import numpy as np
import cv2
import matplotlib.pyplot as plt

# Load the input image
image = cv2.imread('download.jpg', 0)

# Define horizontal and vertical kernels for convolution
kernel_h = np.array([1, 0, -1])  # Horizontal edge detection
kernel_v = np.array([1, 0, -1]).reshape(-1, 1)  # Vertical edge detection

# Perform 1-D convolution along the horizontal axis
convolve_h = np.convolve(image.flatten(), kernel_h, mode='same').reshape(image.shape)

# Perform 1-D convolution along the vertical axis
convolve_v = np.convolve(image.flatten(), kernel_v.flatten(), mode='same').reshape(image.shape)

# Display the original and convolved images
plt.figure(figsize=(12, 6))

plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

plt.subplot(2, 2, 2)
plt.imshow(convolve_h, cmap='gray')
plt.title('Horizontal Convolution')

plt.subplot(2, 2, 3)
plt.imshow(convolve_v, cmap='gray')
plt.title('Vertical Convolution')

plt.tight_layout()
plt.show()
