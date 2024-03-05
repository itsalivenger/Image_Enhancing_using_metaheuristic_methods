import numpy as np

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

def normalize(imgMatrix, imgMax, imgMin):
  imgMatrix = imgMatrix + 1 - imgMin
  imgMatrix = imgMatrix / imgMax
  return imgMatrix

def denormalize(imgMatrix, imgMax, imgMin):
    imgMatrix = imgMatrix * imgMax
    imgMatrix = imgMatrix + imgMin
    return imgMatrix - 1