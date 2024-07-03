import cv2
import numpy as np

img = cv2.imread("download.jpg", cv2.IMREAD_GRAYSCALE)  # Load as grayscale

c = 45  # Adjust constant for desired effect

# Inverse Logarithmic transformation
inverse_log_img = np.exp(img.astype(np.float32) / c) - 1
cv2.imshow("Original", img)
cv2.imshow("Inverse Logarithmic", inverse_log_img.astype(np.uint8))  # Convert back to uint8 for display
cv2.waitKey(0)
cv2.destroyAllWindows()
