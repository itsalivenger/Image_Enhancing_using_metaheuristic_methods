import cv2
import numpy as np
import kernels
import functions as fc

imgName = "./cat.webp"
img = cv2.imread(imgName)
# gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
IMG_MAX = img.max()
IMG_MIN = img.min()

# img = cv2.normalize(img, None, 0, 1.0, cv2.NORM_MINMAX, dtype=cv2.CV_32F)
img = fc.normalize(img, IMG_MAX, IMG_MIN)

#dividing the image channels
red_channel = img[..., 0]
green_channel = img[..., 1]
blue_channel = img[..., 2]

kernel = kernels.anotherTestKernel
# kernel normalization
# kernel = cv2.normalize(kernel, None, 0, 1.0, cv2.NORM_MINMAX, dtype=cv2.CV_32F)
kernel = fc.normalize(kernel, kernel.max(), kernel.min())

convR = fc.convolutionProduct(red_channel, kernel)
convG = fc.convolutionProduct(green_channel, kernel)
convB = fc.convolutionProduct(blue_channel, kernel)

newImg = np.zeros_like(img)
newImg[..., 0] = convR
newImg[..., 1] = convG
newImg[..., 2] = convB

# newImg = np.dstack((convR, convG, convB))

# for channelNum in range(0, img.shape[2]):
#     newImg[..., channelNum] = fc.convolutionProduct(img[..., channelNum]
#     , kernels.gaussian)
    
# newImg = fc.denormalize(newImg, IMG_MAX, IMG_MIN)
# newImg = newImg.reshape((img.shape[0], img.shape[1], img.shape[2]))
newImg = newImg.astype(np.uint8)
print(newImg.shape, img.shape)
print("done")

# cv2.imwrite("edge_detection.jpg", newImg)
cv2.imshow(imgName, newImg)
cv2.waitKey()