import numpy as np

class Agent:
    def __init__(self, dimension):
        self.position = np.zeros(dimension)
    
    def __str__(self):
        return self.position

    def initialise(self, interval):
        self.position = np.array([interval[i][0] + np.random.rand() * (interval[i][1] - interval[i][0]) for i in range(len(interval))])
    
    def keepInInterval(self, interval):
        for i in range(len(self.position)):
            if self.position[i] < interval[i][0]:
                self.position[i] = interval[i][0]
            if self.position[i] > interval[i][1]:
                self.position[i] = interval[i][1]

    def updatePosition(self, newPos):
        self.position = newPos

    def getPosition(self):
        return self.position

def sineCosAlg(agents_count, maxIter, interval, b, cost):
    dimension = len(interval)
    agents = [Agent(dimension) for _ in range(agents_count)]

    # Initialization of the population
    for agent in agents:
        agent.initialise(interval)

    for t in range(maxIter):
        # Getting the best agent
        bestAgent = getBestAgent(agents, cost)
        bestPos = bestAgent.getPosition()

        # Updating the agents' positions
        for agent in agents:
            pos = agent.getPosition()
            r1 = b - b * (t / maxIter)
            r2 = 2 * np.pi * np.random.rand()
            r3 = 2 * np.random.rand()
            r4 = np.random.rand()
            if r4 >= 0.5:
                newPos = pos + r1 * np.cos(r2) * np.abs(r3 * bestPos - pos)
            else:
                newPos = pos + r1 * np.sin(r2) * np.abs(r3 * bestPos - pos)
            agent.updatePosition(newPos)
            agent.keepInInterval(interval)

    return getBestAgent(agents, cost).getPosition(), agents

# Search for the best agent
def getBestAgent(agents, cost):
    bestAgent = min(agents, key=lambda agent: cost(agent.getPosition()))
    return bestAgent

# i will replace it with the EME function later, this is just for testing
# the minimum of the function f(X) = X1 ^ 2 + X2 ^ 2 + x3 ^ 2
# def cost(x):
#     return func(x)

# def printAgents(agents):
#     for i in range(len(agents)):
#         agents[i].printAgentPos()

# agents = sineCosAlg(10, 100, INTERVAL, 2)

# a = getBestAgent(agents).position
# print(cost(a), a)