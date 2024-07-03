import cv2
import numpy as np

img=cv2.imread('LowC.jpeg',0)

minmax_img=np.zeros((img.shape[0],img.shape[1]),dtype='uint8')

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        minmax_img[i,j]=255*(img[i,j]-np.min(img)/(np.max(img)-np.min(min)))
        

cv2.imshow('original Image',img)
cv2.imshow('MinMax',minmax_img)

cv2.waitKey(0)
