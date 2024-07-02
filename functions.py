import numpy as np
import cv2


def convolution2D(imgMatrix, kernel):
    img = np.array(imgMatrix)
    kHeight, kWidth = kernel.shape[0], kernel.shape[1]
    convoledImg = np.zeros((img.shape[0], img.shape[1]))

    for i in range(kHeight // 2, img.shape[0] - kHeight // 2 - 1):
        for j in range(kWidth // 2, img.shape[1] - kWidth // 2 - 1):
                window = img[i - kHeight // 2 : i + kHeight // 2 + 1, j - kWidth // 2: j + kWidth // 2 + 1]
                convoledImg[i, j] = int(getMatrixSum(window * kernel))
    
    convoledImg = np.clip(convoledImg, 0, 255)
    return convoledImg.astype(np.uint8)

def getMatrixSum(matrix):
    sum = 0
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            sum += matrix[i][j]
    return sum

def normalize(imgMatrix):
  minVal = np.min(imgMatrix.ravel())
  maxVal = np.max(imgMatrix.ravel())
  out = (imgMatrix - minVal) / (maxVal - minVal)
  return out

def denormalize(imgMatrix, imgMax, imgMin):
    imgMatrix = imgMatrix * imgMax
    imgMatrix = imgMatrix + imgMin
    return imgMatrix - 1


def EME(image, n, m):
    # print(image.shape)
    h, w = image.shape
    eme = 0
    k1 = h // n
    k2 = w // m
    
    for i in range(n):
        for j in range(m):
            block = image[i * k1:(i + 1) * k1, j * k2:(j + 1) * k2]
            max_val = np.max(block)
            min_val = np.min(block)
            if min_val > 0:
                eme += np.log(max_val / min_val)
    
    return eme * (20 / (n * m))

def Fitzugh_Nagumo(img):
    b = 1; a = .5; tau = 1e-3; dt = 1e-3

    u = img
    v = 0
    for i in range(5):
        u = (dt / tau) * (u * (u - a) * (1 - u) - v)
        v = v + (dt) * (u - b * v)
    return u

def PSNR(original, enhanced):
    mse = np.mean((original - enhanced) ** 2)
    if mse == 0:
        return float('inf')
    pixel_max = 1.0
    return 20 * np.log10(pixel_max / np.sqrt(mse))

import numpy as np

def CNR(image):
    # Calculate mean pixel intensity
    mean_intensity = np.mean(image)
    
    # Calculate standard deviation of pixel intensity
    std_intensity = np.std(image)
    
    # Calculate CNR
    cnr = mean_intensity / std_intensity
    
    return cnr


def gradient_magnitude(image):
    grad_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    grad_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    grad_magnitude = np.sqrt(grad_x ** 2 + grad_y ** 2)
    return np.mean(grad_magnitude)

