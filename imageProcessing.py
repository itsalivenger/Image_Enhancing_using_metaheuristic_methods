import cv2
import functions as fc
import kernels as ks
import numpy as np
import matplotlib.pyplot as plt
from metaheuristics.PSO import PSO 
from metaheuristics.SineCosAlg import sineCosAlg 
from metaheuristics.FPA import FPA
from metaheuristics.GSA import GSA
import pydicom


directory = "xray2.jpeg"
# dicom_data = pydicom.dcmread(directory)
# img = dicom_data.pixel_array
img = cv2.imread(directory, cv2.IMREAD_GRAYSCALE)

n = 4
m = 4
img = fc.normalize(img)
# img = fc.Fitzugh_Nagumo(img)

u1= cv2.filter2D(img, -1, ks.H1)
u2= cv2.filter2D(img, -1, ks.H2)
u3= cv2.filter2D(img, -1, ks.h3)
u4= cv2.filter2D(img, -1, ks.h4)

def Opt(W):
    w1, w2, w3, w4 = W
    v = (u1 * w1 + u2 * w2 + u3 * w3 + u4 * w4)
    emeVal = 1 / (1 + np.power(fc.EME(v, n, m), 2))
    return emeVal

bounds = np.array([[0, 1], [0, 1], [0, 1], [0, 1]])
dimensions = bounds.shape[0]

# BestPosition, best_value = PSO(100, dimensions, bounds, 100, Opt)
# BestPosition, agents = sineCosAlg(200, 300, bounds, 2, Opt)
# BestPosition, flowers = FPA(40, .1, 1.5, bounds, 150, .8, .01, Opt)
BestPosition, worstPlanet = GSA(100, .5, .5, bounds, 100, 2, Opt)


print(BestPosition)
imgRes = (u1 * BestPosition[0] + u2 * BestPosition[1] + u3 * BestPosition[2] + u4 * BestPosition[3])

# imgRes = 0.0895177 * u1 + 0.01842585 * u2 + 0.20577308 * u3 + 0.9434533 * u4

emeBefore = fc.EME(img, n, m)
emeAfter = fc.EME(imgRes, n, m)


print(f"PSO: Optimized weights: {BestPosition}, EME after: {emeAfter}, EME before: {emeBefore}")


plt.subplot(121), plt.title(f"Before EME({n},{m}) = {emeBefore}:"), plt.imshow(img, cmap='gray')
plt.subplot(122), plt.title(f"after EME({n},{m}) = {emeAfter}:"), plt.imshow(imgRes, cmap='gray')
plt.show()