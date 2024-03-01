import numpy as np

def convolutionProduct(imgMatrix, kernel):
    # kernelSum = getMatrixSum(kernel)
    # if(kernelSum != 1): 
    #     print("Kernel is not compatible, it needs to be normalized!")
    #     exit(0)
    
    currentSubMatrix = []
    finalImage = []
    for i in range(0, len(imgMatrix)):
        finalImage.append([])
        for j in range(0, len(imgMatrix[i])):
            currentSubMatrix.append([getPxl(imgMatrix, i - 1, j - 1), getPxl(imgMatrix, i - 1, j), getPxl(imgMatrix, i - 1, j + 1)])
            currentSubMatrix.append([getPxl(imgMatrix, i, j - 1), getPxl(imgMatrix, i, j), getPxl(imgMatrix, i, j + 1)])
            currentSubMatrix.append([getPxl(imgMatrix, i + 1, j - 1), getPxl(imgMatrix, i + 1, j), getPxl(imgMatrix, i + 1, j + 1)])
            pixelValue = getMatrixSum(matrix1To1Product(currentSubMatrix, kernel))
            finalImage[i].append(pixelValue)
            currentSubMatrix = []
    return finalImage

def getPxl(matrix, i, j):
    if(i < 0 or j < 0 or i > len(matrix) - 1 or j > len(matrix[0]) - 1):
        return 0
    return matrix[i][j]

def matrix1To1Product(matrix1, matrix2):
    result = []
    for i in range(0, len(matrix1)):
        temp = []
        for j in range(0, len(matrix1[i])):
            temp.append(matrix1[i][j] * matrix2[i][j])
        result.append(temp)
    return result


def getMatrixSum(matrix):
    sum = 0
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            sum += matrix[i][j]
    return sum

def scalarMatrixMultiply(scalar, matrix):
    result = []
    for i in range(0, len(matrix)):
        result.append([])
        for j in range(0, len(matrix[0])):
            result[i].append(scalar * matrix[i][j])
    return result

def normalize(imgMatrix, imgMax, imgMin):
  imgMatrix = imgMatrix + 1 - imgMin
  imgMatrix = imgMatrix / imgMax
  return imgMatrix

def denormalize(imgMatrix, imgMax, imgMin):
    imgMatrix *= imgMax
    imgMatrix += imgMin
    return imgMatrix - 1

def createKernel(n):
    kernel = []
    for i in range(0, n):
        kernel.append([])
        for j in range(0, n):
            kernel[i].append(1 * (1 / n))
    return kernel
