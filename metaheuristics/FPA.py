import numpy as np
from costFct import func, INTERVAL

class Flower:
    def __init__(self):
        self.position = []

    def initialize(self, interval):
        for i in range(len(interval)):
            self.position.append(interval[i][0] + np.random.rand() * (interval[i][1] - interval[i][0]))
    
    def localPolli(self, pop, interval):
        n = len(self.position)
        for i in range(len(self.position)):
            r = np.random.rand()
            i_1 = np.random.randint(0, n)
            i_2 = np.random.randint(0, n)
            while i_2 == i_1:
                i_2 = np.random.randint(0, n)
            a = self.position[i] + r * (pop[i_1].position[i] - pop[i_2].position[i])
            if(a < interval[i][0]):
                self.position[i] = interval[i][0]
            elif(a > interval[i][1]):
                self.position[i] = interval[i][1]
            else:
                self.position[i] = a

    def globalPolli(self, best, scalingFact, stepParam, s, interval):
        for i in range(len(self.position)):
            a = self.position[i] + scalingFact * Levy(stepParam, s) * (self.position[i] - best.position[i])
            if(a < interval[i][0]):
                self.position[i] = interval[i][0]
            elif(a > interval[i][1]):
                self.position[i] = interval[i][1]
            else:
                self.position[i] = a




# functions
def Levy(stepParam, s):
    return stepParam * gamma(stepParam) * np.sin(np.pi * stepParam / 2) / (np.pi * np.power(s, 1 + stepParam))


def gamma(n):
    p = 1
    for i in range(2, n):
        p *= i
    return p

def printFlowers(flowers):
    for flower in flowers:
        print(flower.position)

def getBestFlower(flowers):
    best = flowers[0]
    for flower in flowers:
        if(func(flower.position) < func(best.position)):
            best = flower
    return best

def FPA(flowerCount, scalingFact, stepParam, interval, maxIter, p, s):
    flowers = []
    # initialization of flower population
    for i in range(flowerCount):
        flower = Flower()
        flower.initialize(interval)
        flowers.append(flower)


    best = getBestFlower(flowers)
    for i in range(maxIter):
        for flower in flowers:
            r = np.random.rand()
            if(r <= p):
                flower.localPolli(flowers, interval)
            else:
                flower.globalPolli(best, scalingFact, stepParam, s, interval)
        best = getBestFlower(flowers)
    return flowers, best


# FPA(flowerCount, scalingFact, stepParam, interval, maxIter, p, s)
(flowers, best) = FPA(40, .1, 1, INTERVAL, 100, .9, 10)
print(best.position, func(best.position))