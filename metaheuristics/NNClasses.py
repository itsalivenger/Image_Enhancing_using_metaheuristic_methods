class Neuron:
    def __init__(self, weight, bias, value):
        self.weight = weight
        self.bias = bias
        self.value = value
    
    def __str__(self):
        return f"weight: {self.weight}, bias: {self.bias}, value: {self.value}"
    
class Layer:
    def __init__(self):
        self.neurons = []
    
class Neural_Network:
    def __init__(self):
        self.layers = []