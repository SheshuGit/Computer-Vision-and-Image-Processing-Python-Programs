import cv2
import numpy as np

# Define input image and kernel
input_image = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 255, 255, 255, 0, 0, 0, 255],
    [0, 255, 255, 255, 0, 0, 0, 0],
    [0, 255, 255, 255, 0, 255, 0, 0],
    [0, 0, 255, 0, 0, 0, 0, 0],
    [0, 0, 255, 0, 0, 255, 255, 0],
    [0, 255, 0, 255, 0, 0, 255, 0],
    [0, 255, 255, 255, 0, 0, 0, 0]], dtype="uint8")

kernel = np.array([
        [0, 1, 0],
        [1, -1, 1],
        [0, 1, 0]], dtype="int")

# Apply hit-or-miss transform
output_image = cv2.morphologyEx(input_image, cv2.MORPH_HITMISS, kernel)

# Scale up input image and kernel for visualization
rate = 50
kernel_scaled = cv2.resize((kernel + 1) * 127, None, fx=rate, fy=rate, interpolation=cv2.INTER_NEAREST).astype(np.uint8)
input_image_scaled = cv2.resize(input_image, None, fx=rate, fy=rate, interpolation=cv2.INTER_NEAREST)
output_image_scaled = cv2.resize(output_image, None, fx=rate, fy=rate, interpolation=cv2.INTER_NEAREST)

# Display images
cv2.imshow("Kernel", kernel_scaled)
cv2.imshow("Original", input_image_scaled)
cv2.imshow("Hit or Miss", output_image_scaled)
cv2.waitKey(0)
cv2.destroyAllWindows()
