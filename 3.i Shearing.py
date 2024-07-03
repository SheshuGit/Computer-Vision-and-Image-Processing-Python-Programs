import cv2
import numpy as np


img = cv2.imread("download.jpg")

shear_x = 0  # Horizontal shear factor
shear_y = 0.2  # Vertical shear factor

# Shearing matrix
M = np.array([[1, shear_x, 0], [shear_y, 1, 0]], dtype=np.float32)

# Apply transformation
sheared_img = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))

cv2.imshow("Original", img)
cv2.imshow("Sheared", sheared_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
