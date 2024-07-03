import numpy as np
import cv2
from matplotlib import pyplot as plt

# Load the image
img = cv2.imread('apple.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Thresholding using Otsu's method
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Morphological closing to remove noise
kernel = np.ones((2, 2), np.uint8)
closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)

# Finding sure background area
sure_bg = cv2.dilate(closing, kernel, iterations=3)

# Finding sure foreground area
dist_transform = cv2.distanceTransform(sure_bg, cv2.DIST_L2, 3)
ret, sure_fg = cv2.threshold(dist_transform, 0.1 * dist_transform.max(), 255, 0)

# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)

# Marker labeling
ret, markers = cv2.connectedComponents(sure_fg)
markers = markers + 1
markers[unknown == 255] = 0

# Apply watershed algorithm
markers = cv2.watershed(img, markers)
img[markers == -1] = [255, 0, 0]

# Display the result
plt.subplot(211), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(212), plt.imshow(thresh, 'gray')

plt.title("Otsu's binary threshold"), plt.xticks([]), plt.yticks([])
plt.tight_layout()
plt.show()
