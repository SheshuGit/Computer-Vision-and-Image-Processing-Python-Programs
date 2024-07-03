import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = 'charlie.png'  
image = cv2.imread(image_path, 0)


box_filtered_image = cv2.blur(image, (5, 5), 1)
plt.imshow(box_filtered_image, cmap='gray')
plt.title('box Filter')
plt.axis('off')
plt.show()

