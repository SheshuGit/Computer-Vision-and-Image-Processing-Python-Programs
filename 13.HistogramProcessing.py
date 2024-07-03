import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image in grayscale
image = cv2.imread('download.jpg', cv2.IMREAD_GRAYSCALE)

# Histogram stretching
def histogram_stretching(image, new_min, new_max):
    min_val = np.min(image)
    max_val = np.max(image)
    stretched_image = ((image - min_val) * (new_max - new_min) / (max_val - min_val)) + new_min
    return stretched_image.astype(np.uint8)

# Histogram sliding
def histogram_sliding(image, slide_amount):
    slid_image = np.clip(image + slide_amount, 0, 255)
    return slid_image.astype(np.uint8)

# Histogram shrinking
def histogram_shrinking(image, shrink_amount):
    min_val = np.min(image)
    max_val = np.max(image)
    shrunk_image = ((image - min_val) * (255 - shrink_amount) / (max_val - min_val))
    return shrunk_image.astype(np.uint8)

# Low contrast (brightness reduction)
def low_contrast(image, factor):
    contrast_image = np.clip(image / factor, 0, 255)
    return contrast_image.astype(np.uint8)

# Apply the operations
stretched_image = histogram_stretching(image, 0, 255)
slid_image = histogram_sliding(image, 30) # Slide the histogram by 30 units
shrunk_image = histogram_shrinking(image, 230) # Shrink the histogram by 100 units
low_contrast_image = low_contrast(image, 2) # Reduce contrast (increase brightness)

# Display the original and processed images
plt.figure(figsize=(14, 8))

# Original image
plt.subplot(2, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# Stretched image
plt.subplot(2, 3, 2)
plt.imshow(stretched_image, cmap='gray')
plt.title('Stretched Histogram')
plt.axis('off')

# Slid image
plt.subplot(2, 3, 3)
plt.imshow(slid_image, cmap='gray')
plt.title('Slid Histogram')
plt.axis('off')

# Shrunk image
plt.subplot(2, 3, 4)
plt.imshow(shrunk_image, cmap='gray')
plt.title('Shrunk Histogram')
plt.axis('off')

# Low contrast image
plt.subplot(2, 3, 5)
plt.imshow(low_contrast_image, cmap='gray')
plt.title('Low Contrast')
plt.axis('off')

plt.show()