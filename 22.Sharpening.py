
import cv2
import numpy as np
import matplotlib.pyplot as plt

org=cv2.imread('moon.jpeg')

plt.imshow(org)
plt.axis('off')
plt.show()



sharpen_filter=np.array([[0,-2,0],[-1,5,-1],[0,-2,0]])

sharp_image=cv2.filter2D(org,-1,sharpen_filter)
plt.imshow(sharp_image)
plt.show()