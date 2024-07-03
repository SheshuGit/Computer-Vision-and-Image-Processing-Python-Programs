
import cv2
import numpy as np
import matplotlib.pyplot as plt

f=cv2.imread('cosine.jpg',0)

F=np.fft.fft2(f)
Fshift=np.fft.fftshift(F)
plt.imshow(np.log1p(np.abs(Fshift)),cmap='gray')
plt.axis('off')
plt.show()

#ButterWorth Low Pass Filter

M,N=f.shape
H=np.zeros((M,N),dtype=np.float32)
D0=10#cutoff frequency
n=10 #order
for u in range(M):
    for v in range(N):
        D = np.sqrt((u-M/2)**2+(v-N/2)**2)
        H[u,v]=1/(1+(D/D0)**n)

plt.imshow(H,cmap='gray')
plt.axis('off')
plt.show()

#frequency domain image filters
Gshift=Fshift * H
G=np.fft.ifftshift(Gshift)
g=np.abs(np.fft.ifft2(G))

plt.imshow(g,cmap='gray')
plt.axis('off')
plt.show()

#ButterWorth High Pass Filter
HPF=np.zeros((M,N),dtype=np.float32)
D0=10#cutoff frequency
n=1 #order
for u in range(M):
    for v in range(N):
        D = np.sqrt((u-M/2)**2+(v-N/2)**2)
        HPF[u,v]=1/(1+(D0/D)**n)

plt.imshow(HPF,cmap='gray')
plt.axis('off')
plt.show()

#frequency domain image filters
Gshift=Fshift * HPF
G=np.fft.ifftshift(Gshift)
g=np.abs(np.fft.ifft2(G))

plt.imshow(g,cmap='gray')
plt.axis('off')
plt.show()



        