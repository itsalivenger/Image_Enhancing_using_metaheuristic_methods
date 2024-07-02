import numpy as np


class Planet:
    def __init__(self):
        self.position = []
        self.velocity = []
        self.active_mass = 1
        self.passive_mass = 1
        self.inertia_mass = 1
        self.fitness = 0

    def __str__(self):
        return f"mass: {self.active_mass}"

    def initialize(self, interval):
        self.velocity = np.zeros(len(interval))  # initialization of velocity
        self.position = [interval[i][0] + np.random.rand() * (interval[i][1] - interval[i][0]) for i in range(len(interval))]

    def update_fitness(self, fitness_func):
        self.fitness = fitness_func(self.position)

    def calculate_mass(self, qi, sqi):
        mass = qi / sqi
        self.active_mass = self.passive_mass = self.inertia_mass = mass

    def bind_within_interval(self, interval):
        self.position = [max(min(self.position[i], interval[i][1]), interval[i][0]) for i in range(len(interval))]


def euclidean_distance(vect1, vect2):
    return np.linalg.norm(np.array(vect1) - np.array(vect2))


def calculate_forces(planets, current_planet, i, Gt, P):
    forces = np.zeros(len(current_planet.position))
    eps = 1e-4

    for j, planet in enumerate(planets):
        if j != i:
            R = euclidean_distance(current_planet.position, planet.position)
            for k in range(len(current_planet.position)):
                forces[k] += Gt * (current_planet.passive_mass * planet.active_mass) * (planet.position[k] - current_planet.position[k]) / (R + eps) ** P
    return forces


def update_position(forces, planet):
    new_position = []
    Mii = planet.inertia_mass
    for i in range(len(forces)):
        a = np.random.rand() * forces[i] / Mii
        v = np.random.rand() * planet.velocity[i] + a
        pos_i = planet.position[i] + v
        new_position.append(pos_i)
    return new_position


def get_best_worst_fitness(planets):
    best = min(planets, key=lambda p: p.fitness).fitness
    worst = max(planets, key=lambda p: p.fitness).fitness
    return best, worst


def GSA(planets_count, alpha, G0, interval, Tmax, P, fitness_func):
    planets = [Planet() for _ in range(planets_count)]

    for planet in planets:
        planet.initialize(interval)
        planet.update_fitness(fitness_func)

    best_fitness, worst_fitness = get_best_worst_fitness(planets)
    prev_sqi = sum((planet.fitness + 0.01 - worst_fitness) / (best_fitness - worst_fitness + 0.01) for planet in planets)

    for t in range(Tmax):
        Gt = G0 * np.exp(-alpha * t / Tmax)
        best_fitness, worst_fitness = get_best_worst_fitness(planets)
        sqi = sum((planet.fitness + 0.01 - worst_fitness) / (best_fitness - worst_fitness + 0.01) for planet in planets)

        for i, planet in enumerate(planets):
            qi = (planet.fitness + 0.01 - worst_fitness) / (best_fitness - worst_fitness + 0.01)
            planet.calculate_mass(qi, prev_sqi)

            Fi = calculate_forces(planets, planet, i, Gt, P)
            planet.position = update_position(Fi, planet)
            planet.update_fitness(fitness_func)
            planet.bind_within_interval(interval)

        prev_sqi = sqi

    sorted_planets = sorted(planets, key=lambda p: p.fitness)
    return sorted_planets[0].position, sorted_planets[-1].position


# best, worst = GSA(50, .5, 1, [[-5, 5], [-5, 5]], 100, 2, fc.sphere)

# print(best, worst)