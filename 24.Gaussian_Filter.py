import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
                  
f = cv2.imread('rubik.png', 0)

F = np.fft.fft2(f)
Fshift = np.fft.fftshift(F)
plt.imshow(np.log1p(np.abs(Fshift)), cmap='gray')
plt.axis('off')
plt.show()

# Gaussian Low Pass Filter

M, N = f.shape
H = np.zeros((M, N), dtype=np.float32)
D0 = 10  # cutoff frequency
for u in range(M):
    for v in range(N):
        D = np.sqrt((u - M / 2) ** 2 + (v - N / 2) ** 2)
        H[u, v] = np.exp(-(D ** 2) / (2 * (D0 ** 2)))

plt.imshow(H, cmap='gray')
plt.axis('off')
plt.show()

# frequency domain image filters
Gshift = Fshift * H
G = np.fft.ifftshift(Gshift)
g = np.abs(np.fft.ifft2(G))

plt.imshow(g, cmap='gray')
plt.axis('off')
plt.show()


# Gaussian High Pass Filter

M, N = f.shape
H = np.zeros((M, N), dtype=np.float32)
D0 = 10  # cutoff frequency
for u in range(M):
    for v in range(N):
        D = np.sqrt((u - M / 2) ** 2 + (v - N / 2) ** 2)
        H[u, v] = np.exp(-(2 * (D0 ** 2)/(D ** 2)))

plt.imshow(H, cmap='gray')
plt.axis('off')
plt.show()

# frequency domain image filters
Gshift = Fshift * H
G = np.fft.ifftshift(Gshift)
g = np.abs(np.fft.ifft2(G))

plt.imshow(g, cmap='gray')
plt.axis('off')
plt.show()