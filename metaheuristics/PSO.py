import numpy as np
# from metaheuristics.costFct import INTERVAL
# from plotting import Plot_Particles


PARTICLE_COUNT = 100
MAX_ITER = 100

def printParticles(flock):
    for i in range(len(flock)):
        print(flock[i].position)


class Particle:
    def __init__(self, step, func):
        self.position = []
        self.best = []
        self.step = step
        self.func = func
    
    def initialize(self, interval):
        for i in range(len(interval)):
            self.position.append(interval[i][0] + np.random.rand() * (interval[i][1] - interval[i][0]))
            self.best = self.position[:]

    def move(self, best):
        for i in range(len(self.position)):
            self.position[i] += self.step * (-1 if self.position[i] <= 0 else 1) 
        self.evaluate()
        
        for i in range(len(self.best)):
            self.position[i] += self.step * (-1 if self.position[i] > self.best[i] else 1) 
        self.evaluate()
            
        for i in range(len(best)):
            self.position[i] += self.step * (-1 if self.position[i] > best[i] else 1) 
        self.evaluate()

    def evaluate(self):
        if self.func(self.position) < self.func(self.best):
            self.best = self.position[:]
    
    def keepInInterval(self, interval):
        for i in range(len(interval)):
            if(self.position[i] > interval[i][1]):
                self.position[i] = interval[i][1]
            
            if(self.position[i] < interval[i][0]):
                self.position[i] = interval[i][0]




def PSO(n, step, interval, MAX_ITER, func):
    flock = []
    TeamBest = []
    for i in range(len(interval)):
        TeamBest.append((interval[i][0] + interval[i][1]) / 2)
    # initalization
    for i in range(n):
        particle = Particle(step, func)
        particle.initialize(interval)
        if(func(particle.position) < func(TeamBest)):
            TeamBest = particle.position[:]
        flock.append(particle)

        

    
    
    for i in range(MAX_ITER):
        for j in range(len(flock)):
            flock[j].move(TeamBest)
            flock[j].keepInInterval(interval)
            if(func(flock[j].position) < func(TeamBest)):
                TeamBest = flock[j].position[:]

    return (flock, TeamBest)

# a, bestSol = PSO(PARTICLE_COUNT, .1, INTERVAL, MAX_ITER)
# print("final result")
# printParticles(a)

# b = []
# for i in range(len(a)):
#     b.append(a[i].position)

# printParticles(a)
# print(func(bestSol), bestSol)
# Plot_Particles(func, b)
