import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = 'charlie.png'  
image = cv2.imread(image_path, 0)


gaussian_filtered_image = cv2.GaussianBlur(image, (5, 5), 1)
plt.imshow(gaussian_filtered_image, cmap='gray')
plt.title('Gaussian Filter')
plt.axis('off')
plt.show()

