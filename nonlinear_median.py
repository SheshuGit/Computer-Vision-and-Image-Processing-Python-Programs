import cv2
import matplotlib.pyplot as plt

img = cv2.imread('mountain.jpeg',0)

median_blur = cv2.medianBlur(img, 3)


plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(median_blur, cmap='gray')
plt.title('Blurred Image (Median filter)')
plt.axis('off')

plt.show()