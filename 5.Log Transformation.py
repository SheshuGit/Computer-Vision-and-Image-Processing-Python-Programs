import cv2
import numpy as np

img = cv2.imread("download.jpg", cv2.IMREAD_GRAYSCALE)  # Load as grayscale

c = 45  # Adjust constant for desired effect

# Logarithmic transformation
log_img = c * np.log(1 + img)

cv2.imshow("Original", img)
cv2.imshow("Logarithmic", log_img.astype(np.uint8))  # Convert back to uint8 for display
cv2.waitKey(0)
cv2.destroyAllWindows()
