import numpy as np
import cv2

# Load the image
image = cv2.imread('noisysalterpepper.png', 0)  # Read in grayscale mode

# Compute the 2D Fourier Transform
f = np.fft.fft2(image)
fshift = np.fft.fftshift(f)

# Define the notch filter parameters
rows, cols = image.shape
crow, ccol = rows // 2, cols // 2  # Center coordinates
radius = 50  # Radius of the notch filter

# Create a mask for the notch filter
mask = np.ones((rows, cols), dtype=np.uint8)
x, y = np.ogrid[:rows, :cols]
mask_area = (x - crow) * 2 + (y - ccol) * 2 <= radius ** 2
mask[mask_area] = 0

# Apply the notch filter
fshift_filtered = fshift * mask
f_filtered = np.fft.ifftshift(fshift_filtered)
filtered_image = np.abs(np.fft.ifft2(f_filtered))

# Display the original and filtered images
cv2.imshow('Original Image', image)
cv2.imshow('Filtered Image', filtered_image.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()