import numpy as np
from costFct import func as fitnessFunc, INTERVAL 
from plotFct import plotFct

class Planet:
    def __init__(self):
        self.position = []
        self.velocity = []
        self.activeMass = 1
        self.passiveMass = 1
        self.inertiaMass = 1
        self.fitness = 0

    def __str__(self):
        return f"mass: {self.activeMass}"

    def initialize(self, interval):
        self.velocity = np.zeros(len(interval)) # initialization of velocity
        for i in range(len(interval)):
            self.position.append(interval[i][0] + np.random.rand() * (interval[i][1] - interval[i][0])) # initialization of position
    
    def updateFitness(self):
        self.fitness = fitnessFunc(self.position)
    
    def calculateMass(self, qi, sqi):
        a = qi / sqi
        self.activeMass = a
        self.passiveMass = a
        self.inertiaMass = a

    def bindWithinInterval(self, interval):
        for i in range(len(interval)):
            if(self.position[i] > interval[i][1]):
                self.position[i] = interval[i][1]
            if(self.position[i] < interval[i][0]):
                self.position[i] = interval[i][0]



def euclidienDistance(vect1, vect2):
    d = 0
    for i in range(len(vect1)):
        d += pow((vect1[i] - vect2[i]), 2)
    return np.sqrt(d)

def calculateForces(planets, currentPlanet, i, Gt, P):
    forces = np.zeros(len(currentPlanet.position))
    eps = .0001
    
    for j in range(len(planets)):
        if(j != i):
            R = euclidienDistance(currentPlanet.position, planets[j].position)
            for k in range(len(planets[i].position)): # looping throught the dimension of the vectors
                forces[k] += Gt * (currentPlanet.passiveMass * planets[j].activeMass) * (planets[j].position[k] - currentPlanet.position[k]) / (R + eps) ** P
    return forces



def calcPos(forces, planet):
    x = []
    Mii = planet.inertiaMass
    for i in range(len(forces)):
        a = np.random.rand() * forces[i] / Mii
        v = np.random.rand() * planet.velocity[i] + a
        posi = planet.position[i] + v
        x.append(posi)
    return x

def getBestWorstFitness(planets):
    best = worst = planets[0].fitness
    for i in range(len(planets)):
        if(planets[i].fitness < best):
            best = planets[i].fitness
        
        if(planets[i].fitness > worst):
            worst = planets[i].fitness
    return (best, worst)

def printPlanets(planets):
    for i in range(len(planets)):
        print(planets[i].position)
        print(f"fitness: {planets[i].fitness}", f"mass: {planets[i].passiveMass}")

def sort(tab):
  planets = tab 
  for i in range(len(planets)):
    swapped = False
    for j in range(len(planets) - i - 1):
      if planets[j].fitness > planets[j + 1].fitness:
        planets[j], planets[j + 1] = planets[j + 1], planets[j]
        swapped = True
        
    if not swapped:
      break

  return planets





def GSA(planetsCount, alpha, G0, interval, Tmax, P):
    planets = []

    # initialization and fitness evaluation
    for i in range(planetsCount):
        planet = Planet()
        planet.initialize(interval)
        planet.updateFitness()
        planets.append(planet)

    # printPlanets(planets)
    # print("init")
    
    # setting best, worst fitness and sum of qi = (fitnessFunc(planet[i].position) - bestFitness) / worstFitness - bestFitness
    bestFitness, worstFitness = getBestWorstFitness(planets)

    prevSqi = 0
    for i in range(len(planets)):
        prevSqi += (fitnessFunc(planets[i].position) + .01 - worstFitness) / (bestFitness - worstFitness)
    
    # start of the time flow t -> Tmax 
    for t in range(Tmax):
        Gt = G0 * np.exp(-alpha * t / Tmax) # init of G0
        bestFitness, worstFitness = getBestWorstFitness(planets) # init ta3 best/worst fitness
        sqi = 0 # hada 3la qbel somme des sqi

        # for each t, we update fitness, calculate the sum of the qi for the next iteration
        # calculate masses, forcesm velocities and updating positions of objects.
        for i in range(planetsCount):
            qi = (fitnessFunc(planets[i].position) + .01 - worstFitness) / (bestFitness - worstFitness)
            sqi += qi
            planets[i].calculateMass(qi, prevSqi)

            Fi = calculateForces(planets, planets[i], i, Gt, P)
            planets[i].position = calcPos(Fi, planets[i])
            planets[i].updateFitness()
            planets[i].bindWithinInterval(interval)
            
        prevSqi = sqi

    return planets

# GSA(planetsCount, alpha, G0, interval, Tmax, P)
planets = GSA(100, 20, 50, INTERVAL, 40, 2)


best, worst = getBestWorstFitness(planets)
printPlanets(sort(planets))
print(best, worst)


# plotting
x = []
y = []
for i in range(len(planets)):
    x.append(planets[i].position[0])
    y.append(planets[i].position[1])

plotFct(x, y, fitnessFunc)