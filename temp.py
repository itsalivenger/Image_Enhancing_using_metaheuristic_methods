import cv2
import functions as fc
import kernels as ks
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt

imageName = "cameraBruit.png"
kernel = ks.blur

img = cv2.imread(imageName, cv2.IMREAD_GRAYSCALE)
# img = cv2.imread("cat.webp")

n = 4
normalizedImg = fc.normalize(img)

# normalized images
# u1 = fc.convolution2D(fc.normalize(img, imgMax, imgMin), np.array(ks.h1))
# u2 = fc.convolution2D(fc.normalize(img, imgMax, imgMin), np.array(ks.h2))
# u3 = fc.convolution2D(fc.normalize(img, imgMax, imgMin), np.array(ks.h3))
# u4 = fc.convolution2D(fc.normalize(img, imgMax, imgMin), np.array(ks.h4))

u1 = cv2.filter2D(normalizedImg, -1, np.array(kernel))


plt.subplot(121),plt.title("after:"), plt.imshow(u1, cmap = 'gray') 
plt.subplot(122),plt.title("Before:"), plt.imshow(img, cmap = 'gray')
plt.savefig(f"image_gaussian.png")
plt.show()

# u2 = fc.convolution2D(img, np.array(ks.h2))
# u3 = fc.convolution2D(img, np.array(ks.h3))
# u4 = fc.convolution2D(img, np.array(ks.h4))

# u1= cv2.filter2D(img, -1, np.array(ks.h1))
# u2= cv2.filter2D(img, -1, np.array(ks.h2))
# u3= cv2.filter2D(img, -1, np.array(ks.h3))
# u4= cv2.filter2D(img, -1, np.array(ks.h4))

# w1=.02
# w2=.0
# w3=0.1
# w4=.86

# v = (u1 * w1 + u2 * w2 + u3 * w3 + u4 * w4) 


# emeVal = fc.EME(v, n)
# v = fc.denormalize(v, imgMax, imgMin)
# v = v.astype(np.uint8)

# for channelNum in range(0, img.shape[2]):
#     new_image[..., channelNum] = fc.convolution2D(img[..., channelNum], kernel)

# cv2.imshow("image", u1)
# cv2.waitKey()
# cv2.imshow("image", u3)
# cv2.waitKey()
# cv2.imshow("image", u2)
# cv2.waitKey()
# cv2.imshow("image", u3)
# cv2.waitKey()


# pour la représentation en niveau de gris

# print(emeVal)

# plt.subplot(121),plt.title("Before:"), plt.imshow(img, cmap = 'gray')
# plt.subplot(122),plt.title("After:"), plt.imshow(v, cmap = 'gray')
# plt.show()
