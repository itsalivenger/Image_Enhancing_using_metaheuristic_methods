import numpy as np
import matplotlib.pyplot as plt

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


def EME(image, n):
    imgH, imgW = image.shape

    blocksX = imgW // n
    blocksY = imgH // n

    EMESum = 0
    for i in range(n):
        for j in range(n):
            block = image[i * blocksX:(i + 1) * blocksX, j * blocksY:(j + 1) * blocksY]
            # print(block, "/newline")
            blockMin = np.min(block)
            blockMax = np.max(block)

            if(blockMin > 0):
                EMESum += 20 * np.log(blockMax / blockMin)
    
    EMESum /= blocksX * blocksY
    return EMESum

def Fitzugh_Nagumo(img):
    b = 1; a = .5; tau = 1e-3; dt = 1e-3
    I = img.astype(np.float64) / 255.0

    u = I
    v = 0
    for i in range(5):
        u = (dt / tau) * (u * (u - a) * (1 - u) - v)
        v = v + (dt) * (u - b * v)
    return u