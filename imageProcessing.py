import cv2
import functions as fc
import kernels as ks
import numpy as np
import matplotlib.pyplot as plt
from metaheuristics.PSO import PSO 

img = cv2.imread("cameraBruit.png", cv2.IMREAD_GRAYSCALE)
# img = cv2.imread("cat.webp")

n = 4
img = fc.normalize(img)
# imgRes = fc.convolution2D(img, np.array(ks.emboss))
u1= cv2.filter2D(img, -1, np.array(ks.h1))
u2= cv2.filter2D(img, -1, np.array(ks.h2))
u3= cv2.filter2D(img, -1, np.array(ks.h3))
u4= cv2.filter2D(img, -1, np.array(ks.h4))

def Opt(W):
    w1 = W[0]
    w2 =W[1]
    w3 = W[2]
    w4 = W[3]

    v = (u1 * w1 + u2 * w2 + u3 * w3 + u4 * w4)
    v = fc.Fitzugh_Nagumo(v)

    emeVal = 1 / (1 + fc.EME(v, n) ** 2)
    return emeVal

flock, teamBest = PSO(40, .05, [[0, 1], [0, 1], [0, 1], [0, 1]], 40, Opt)

print(teamBest)
imgRes = (u1 * teamBest[0] + u2 * teamBest[1] + u3 * teamBest[2] + u4 * teamBest[3]) 

plt.subplot(122),plt.title("Before:"), plt.imshow(img, cmap = 'gray')
plt.subplot(121),plt.title("After:"), plt.imshow(imgRes, cmap = 'gray')
plt.show()
