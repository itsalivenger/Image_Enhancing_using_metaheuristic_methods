import numpy as np

class Particle:
    def __init__(self, dimensions, func, w=0.5, c1=1, c2=2):
        self.position = np.random.rand(dimensions)
        self.velocity = np.random.rand(dimensions) * 0.1  # Small initial velocity
        self.best_position = np.copy(self.position)
        self.best_value = float('inf')
        self.func = func
        self.w = w 
        self.c1 = c1 
        self.c2 = c2 

    def update_velocity(self, global_best):
        inertia = self.w * self.velocity
        cognitive = self.c1 * np.random.rand(len(self.position)) * (self.best_position - self.position)
        social = self.c2 * np.random.rand(len(self.position)) * (global_best - self.position)
        self.velocity = inertia + cognitive + social

    def update_position(self, bounds):
        self.position += self.velocity
        self.position = np.clip(self.position, bounds[:, 0], bounds[:, 1])
        
        current_value = self.func(self.position)
        if current_value < self.best_value:
            self.best_value = current_value
            self.best_position = np.copy(self.position)

def PSO(n_particles, dimensions, bounds, max_iter, func):
    particles = [Particle(dimensions, func) for _ in range(n_particles)]
    global_best_position = np.random.rand(dimensions)
    global_best_value = float('inf')
    
    for _ in range(max_iter):
        for particle in particles:
            particle.update_velocity(global_best_position)
            particle.update_position(bounds)
            if particle.best_value < global_best_value:
                global_best_value = particle.best_value
                global_best_position = np.copy(particle.best_position)
    
    return global_best_position, global_best_value

# bounds = np.array([[0, 2], [0, 2], [0, 2], [0, 2]])
# dimensions = bounds.shape[0]

# def example_function(x):
#     return np.sum(x**2) 

# best_position, best_value = PSO(20, dimensions, bounds, 100, example_function)
# print(f"Best position: {best_position}")
# print(f"Best value: {best_value}")
