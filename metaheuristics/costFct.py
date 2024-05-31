import numpy as np

eta=7
dx0, dy0=20, 10
def f(X): # INTERVAL = [[0.1, 2 * np.pi], [0.1, 2 * np.pi], [500, 850], [500, 850]]
    dVx= np.sin(X[0])*X[2] - np.sin(X[1])*X[3]
    dVy= np.cos(X[0])*X[2] - np.cos(X[1])*X[3]
    V = np.sqrt(dVx**2 + dVy**2)
    D0 = np.sqrt(dx0**2 + dy0**2)
    shap = V.shape
    az = np.zeros(shap)
    if np.linalg.norm(V-az) == 0:
      return D0
    else:
      D = D0 ** 2 - (dx0*dVx + dy0*dVy)/(V**2)
      return np.sqrt(D) - eta
    

def logarFc(x):
    return np.log(x[1]) / x[0]


def rosenbrock_function(x , a=1, b=1):
    return (a - x[0])**2 + b * (x[1] - x[0]**2)**2


def sphere(x):
    return x[0] ** 2 + x[1] ** 2

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
    
func = sphere
INTERVAL = [[-5, 10], [-5, 2]]