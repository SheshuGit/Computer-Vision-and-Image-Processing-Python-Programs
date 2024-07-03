import cv2
import numpy as np

def adaptive_median_filter(image, max_kernel_size):
    # Convert image to grayscale if it's colored
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Define a function to apply the adaptive median filter on a pixel
    def apply_filter(x, y):
        # Start with a small kernel size
        kernel_size = 3
        while kernel_size <= max_kernel_size:
            # Define the neighborhood
            x_min = max(0, x - kernel_size // 2)
            x_max = min(image.shape[1] - 1, x + kernel_size // 2)
            y_min = max(0, y - kernel_size // 2)
            y_max = min(image.shape[0] - 1, y + kernel_size // 2)
            
            neighborhood = image[y_min:y_max+1, x_min:x_max+1]
            min_val = np.min(neighborhood)
            max_val = np.max(neighborhood)
            median_val = np.median(neighborhood)
            
            # Check conditions
            if min_val < median_val < max_val:
                if min_val < image[y, x] < max_val:
                    return image[y, x]  # No change needed
                else:
                    return median_val  # Replace with median value
            else:
                kernel_size += 2  # Increase kernel size
        
        # If no condition is met, return the original pixel value
        return image[y, x]
    
    # Create an empty filtered image
    filtered_image = np.zeros_like(image)
    
    # Apply the filter to each pixel
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            filtered_image[y, x] = apply_filter(x, y)
    
    return filtered_image

# Load an image from file
image_path = 'rubik.png'  # Replace with your image path
image = cv2.imread(image_path,0)

# Define the maximum kernel size
max_kernel_size = 9

# Apply adaptive median filter
filtered_image = adaptive_median_filter(image, max_kernel_size)

# Display the original and filtered images
cv2.imshow('Original Image', image)
cv2.imshow('Filtered Image', filtered_image)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()