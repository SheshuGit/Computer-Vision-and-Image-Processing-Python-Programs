import cv2
import matplotlib.pyplot as plt

# Load the input image
img = cv2.imread('download.jpg', 0)

# Apply histogram equalization
equalized_img = cv2.equalizeHist(img)

# Calculate histograms
hist_original = cv2.calcHist([img], [0], None, [256], [0, 256])
hist_equalized = cv2.calcHist([equalized_img], [0], None, [256], [0, 256])

# Create a figure with 2 rows and 2 columns
plt.figure(figsize=(12, 10))

# Plot the original image
plt.subplot(2, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')

# Plot the equalized image
plt.subplot(2, 2, 2)
plt.imshow(equalized_img, cmap='gray')
plt.title('Equalized Image')

# Plot the histogram of the original image
plt.subplot(2, 2, 3)
plt.plot(hist_original, color='black')
plt.title('Original Image Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

# Plot the histogram of the equalized image
plt.subplot(2, 2, 4)
plt.plot(hist_equalized, color='black')
plt.title('Equalized Image Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
