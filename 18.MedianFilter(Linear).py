import cv2
import numpy as np

img = cv2.imread('charlie.png',0)

gaussian_blur = cv2.GaussianBlur(img, (5, 5), 1)
median_blur = cv2.medianBlur(gaussian_blur, 3)

cv2.imshow('Filtered Image', median_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()