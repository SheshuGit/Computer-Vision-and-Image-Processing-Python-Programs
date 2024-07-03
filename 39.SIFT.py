
import cv2 
import matplotlib.pyplot as plt


#reading image
img1 = cv2.imread('sample.jpg',0)  


#keypoints
sift = cv2.SIFT_create()
keypoints_1, descriptors_1 = sift.detectAndCompute(img1,None)

img_1 = cv2.drawKeypoints(img1,keypoints_1,img1)

cv2.imshow("Simpe regions", img_1)
cv2.waitKey(0)