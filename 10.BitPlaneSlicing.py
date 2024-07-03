
import cv2
import numpy as np

img=cv2.imread('download.jpg')
bit_plane=[]
for i in range(8):
    plane=np.bitwise_and(img,2**i)
    bit_plane.append(plane)

for i in range(8):
    cv2.imshow('Bit plane{i}:',bit_plane[i]*255)
    cv2.waitKey(500)
cv2.waitKey(500)
cv2.destroyAllWindows()