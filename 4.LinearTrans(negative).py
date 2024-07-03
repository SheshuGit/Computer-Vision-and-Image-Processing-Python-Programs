import cv2

img = cv2.imread("download.jpg")

# Get maximum intensity value (usually 255 for 8-bit images)
max_intensity = 255

# Negative transformation
negative_img = max_intensity - img

cv2.imshow("Original", img)
cv2.imshow("Negative", negative_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
