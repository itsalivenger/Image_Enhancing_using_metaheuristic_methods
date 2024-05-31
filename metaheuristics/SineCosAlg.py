import numpy as np
from costFct import func, INTERVAL

class Agent:
    def __init__(self, speed):
        self.position = []
        self.speed = speed
    
    def initialise(self, interval):
        for i in range(len(interval)):
            self.position.append(interval[i][0] + np.random.rand() * interval[i][1])
    
    def keepInInterval(self, interval):
        for i in range(len(self.position)):
                if(self.position[i] < interval[i][0]):
                    self.position[i] = interval[i][0]
                
                if(self.position[i] > interval[i][1]):
                    self.position[i] = interval[i][1]
    
    def printAgentPos(self):
        print(self.position)

    def updatePosition(self, newPos):
        self.position = newPos

    def getPosition(self):
        return self.position

def sineCosAlg(agents_count, maxIter, interval, b):
    agents = []

# initalisation of the population
    for i in range(agents_count):
        agents.append(Agent(.2))
        agents[i].initialise(interval)
        # agents[i].printAgentPos()

    for t in range(maxIter):

        # getting best agent
        bestAgent = getBestAgent(agents)

        # updating the agents position
        for i in range(len(agents)):
            pos = agents[i].getPosition()
            for j in range(len(pos)):
                # initialisation of parameters
                r1 = b - b * (t / maxIter)
                r2 = 2 * np.pi * np.random.rand()
                r3 = 2 * np.random.rand()
                r4 = np.random.rand()
                if(r4 >= .5):
                    pos[j] = pos[j] + r1 * np.cos(r2) * np.abs(r3 * bestAgent.getPosition()[j] - pos[j])
                else:
                    pos[j] = pos[j] + r1 * np.sin(r2) * np.abs(r3 * bestAgent.getPosition()[j] - pos[j])
            agents[i].updatePosition(pos) # j'ai ajoute cette line
            agents[i].keepInInterval(interval)
                
    return agents

# search of the best agent
def getBestAgent(agents):
    bestAgent = agents[0]
    bestAgentPos = cost(bestAgent.getPosition())

    for i in range(len(agents)):
        if(cost(agents[i].getPosition()) < bestAgentPos):
            bestAgent = agents[i]
    return bestAgent


# i will replace it with the EME function later, this is just for testing
# the minimum of the function f(X) = X1 ^ 2 + X2 ^ 2 + x3 ^ 2
def cost(x):
    return func(x)

def printAgents(agents):
    for i in range(len(agents)):
        agents[i].printAgentPos()

agents = sineCosAlg(10, 100, INTERVAL, 2)

a = getBestAgent(agents).position
print(cost(a), a)