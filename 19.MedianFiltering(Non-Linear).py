import cv2
import numpy as np
import matplotlib.pyplot as plt


image = cv2.imread('charlie.png', 0)  


kernel_size = 5


Median_filtered_image = cv2.medianBlur(image,kernel_size)

plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(Median_filtered_image, cmap='gray')
plt.title('Median Filter')
plt.axis('off')

plt.show()