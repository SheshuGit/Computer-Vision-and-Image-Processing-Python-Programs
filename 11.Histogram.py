import cv2
import matplotlib.pyplot as plt

img = cv2.imread('download.jpg',0)

hist = cv2.calcHist([img])
plt.plot(hist)
plt.xlabel('Pixel value')
plt.ylabel('Frequency')
plt.show()