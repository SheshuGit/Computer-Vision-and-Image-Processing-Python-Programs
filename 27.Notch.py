import numpy as np
import cv2
import matplotlib.pyplot as plt

def band_reject_filter(shape, center, inner_radius, outer_radius):
    rows, cols=shape
    x=np.arange(cols)
    y=np.arange(rows)
    xx,yy=np.meshgrid(x,y)
    xx=xx-center[0]
    yy=yy-center[1]
    distance=np.sqrt(xx**2+yy**2)
    band_reject=np.ones((rows,cols))
    band_reject[np.where((distance>=inner_radius)&(distance<=outer_radius))]=0
    return band_reject

#loaD THE IMAGE

image=cv2.imread('cosine.jpg',cv2.IMREAD_GRAYSCALE)

#compute the fourier transform

f_transform=np.fft.fft2(image)
f_shift=np.fft.fftshift(f_transform)

#create a band reject filter

rows,cols=image.shape
center=(rows//2, cols//2)
inner_radius=30
outer_radius=60
band_reject=band_reject_filter(image.shape, center, inner_radius, outer_radius)

#apply band reject filter

f_filtered=f_shift*band_reject


#inverse fourier transfom

f_inv_shift=np.fft.ifftshift(f_filtered)
image_filtered=np.fft.ifft2(f_inv_shift)
image_filtered=np.abs(image_filtered)

#convert back to uint8 for display

image_filtered=np.uint8(image_filtered)

#display original and filterd images

plt.figure(figsize=(10,6))
plt.subplot(1,2,1)
plt.imshow(image, cmap='gray')
plt.title('original image')
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(image_filtered, cmap='gray')
plt.title('filtered image')
plt.axis('off')

plt.show()
