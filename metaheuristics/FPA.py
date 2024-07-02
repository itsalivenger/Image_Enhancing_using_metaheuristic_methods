import numpy as np

class Flower:
    def __init__(self, interval):
        self.position = np.array([interval[i][0] + np.random.rand() * (interval[i][1] - interval[i][0]) for i in range(len(interval))])

    def local_pollination(self, population, interval):
        n = len(self.position)
        for i in range(n):
            r = np.random.rand()
            i_1, i_2 = np.random.choice(len(population), 2, replace=False)
            a = self.position[i] + r * (population[i_1].position[i] - population[i_2].position[i])
            self.position[i] = np.clip(a, interval[i][0], interval[i][1])

    def global_pollination(self, best, gamma, lambda_, s, interval):
        for i in range(len(self.position)):
            a = self.position[i] + gamma * levy(lambda_, s) * (self.position[i] - best.position[i])
            self.position[i] = np.clip(a, interval[i][0], interval[i][1])

def levy(lambda_, s):
    return lambda_ * np.math.gamma(lambda_) * np.sin(np.pi * lambda_ / 2) / (np.pi * np.power(s, 1 + lambda_))

def print_flowers(flowers):
    for flower in flowers:
        print(flower.position)

def get_best_flower(flowers, func):
    return min(flowers, key=lambda flower: func(flower.position))

def FPA(flower_count, gamma, lambda_, interval, max_iter, p, s, func):
    flowers = [Flower(interval) for _ in range(flower_count)]
    best = get_best_flower(flowers, func)
    
    for _ in range(max_iter):
        for flower in flowers:
            if np.random.rand() <= p:
                flower.local_pollination(flowers, interval)
            else:
                flower.global_pollination(best, gamma, lambda_, s, interval)
        best = get_best_flower(flowers, func)
    
    return best.position, flowers

# FPA(flowerCount, scalingFact, stepParam, interval, maxIter, p, s)
# (flowers, best) = FPA(40, .1, 1, INTERVAL, 100, .9, 10)