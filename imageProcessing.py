import cv2
import functions as fc
import kernels as ks
import numpy as np
import scipy as sc

img = cv2.imread("cat.webp", cv2.IMREAD_GRAYSCALE)
# img = cv2.imread("cat.webp")

imgMax = img.max()
imgMin = img.min()
# img = fc.normalize(img, imgMax, imgMin)

# kernel = np.array(ks.edgeDetection)

# new_image = np.zeros_like(img)

# normalized images
# u1 = fc.convolution2D(fc.normalize(img, imgMax, imgMin), np.array(ks.h1))
# u2 = fc.convolution2D(fc.normalize(img, imgMax, imgMin), np.array(ks.h2))
# u3 = fc.convolution2D(fc.normalize(img, imgMax, imgMin), np.array(ks.h3))
# u4 = fc.convolution2D(fc.normalize(img, imgMax, imgMin), np.array(ks.h4))

u1 = fc.convolution2D(img, np.array(ks.h1))
u2 = fc.convolution2D(img, np.array(ks.h2))
u3 = fc.convolution2D(img, np.array(ks.h3))
u4 = fc.convolution2D(img, np.array(ks.h4))

# u1 = sc.signal.convolve2d(img, np.array(ks.h1), "full")
# u2 = sc.signal.convolve2d(img, np.array(ks.h2), "full")
# u3 = sc.signal.convolve2d(img, np.array(ks.h3), "full")
# u4 = sc.signal.convolve2d(img, np.array(ks.h4), "full")



w1=0.8
w2=0.4
w3=0.8
w4=0.5

v = u1 * w1 + u2 * w2 + u3 * w3 + u4 * w4

# v = fc.denormalize(v, imgMax, imgMin)
v = v.astype(np.uint8)
# for channelNum in range(0, img.shape[2]):
#     new_image[..., channelNum] = fc.convolution2D(img[..., channelNum], kernel)

# new_image = fc.denormalize(new_image, imgMax, imgMin)

# cv2.imshow("image", u1)
# cv2.waitKey()
# cv2.imshow("image", u3)
# cv2.waitKey()
# cv2.imshow("image", u2)
# cv2.waitKey()
# cv2.imshow("image", u3)
# cv2.waitKey()

cv2.imshow("image", v)
cv2.waitKey()