
import cv2 
import numpy as np

img= cv2.imread('download.jpg')
rows,cols,_=img.shape

pt=np.float32([[50,50],[200,200],[50,200]])
pt2=np.float32([[10,100],[200,50],[50,250]])

M=cv2.getAffineTransform(pt,pt2)
dst=cv2.warpAffine(img,M,(cols,rows))
cv2.imshow("Affine Transform",dst)

cv2.waitKey(0)

cv2.destroyAllWindows() 