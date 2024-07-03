
import cv2
import numpy as np

#create an image with text on it
img = np.zeros((100,400),dtype='uint8')
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'SHESHU',(5,70),font,2,(255),5,cv2.LINE_AA)
img1 = img.copy()

kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
thin = np.zeros(img.shape,dtype='uint8')

while(cv2.countNonZero(img1)!= 0):
    erode = cv2.erode(img1,kernel)
    opening = cv2.morphologyEx(erode,cv2.MORPH_OPEN,kernel)
    subset = erode - opening
    thin = cv2.bitwise_or(subset,thin)
    img1 = erode.copy()
    
cv2.imshow('original',img)
cv2.imshow('thinned',thin)
cv2.waitKey(0)
    
    