import cv2
import numpy as np

img=cv2.imread('erosion_dilation.png',0)
kernel=np.ones((5,5),np.uint8)
opening_result=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
closing_result=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)

cv2.imshow('image',img)
cv2.imshow('opening image',opening_result)
cv2.imshow('closing image',closing_result)
cv2.waitKey(0)
