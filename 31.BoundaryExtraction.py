
import cv2 
import numpy as np

img=cv2.imread('horse.jpg',0)
kernel=np.ones((5,5))

img_erosion=cv2.erode(img,kernel,iterations=1)

bound_img = img - img_erosion

cv2.imshow('input',img)
cv2.imshow('Boundry_Extraction',bound_img)
cv2.waitKey(0)