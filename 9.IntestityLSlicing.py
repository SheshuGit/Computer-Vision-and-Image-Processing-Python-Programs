
import numpy as np
import cv2

img=cv2.imread('download.jpg'0)
row,column=img.shape


min_range=100
max_range=190
for i in range(row):
    for j in range(column):
        if img[i,j]>min_range and img[i,j]<max_range:
            sliced_img[i,j]=255
        else:
            sliced_img[i,j]=0
            

cv2.imshow('Original image',img)
cv2.imshow('sliced_img',sliced_img)
cv2.waitKey(0)