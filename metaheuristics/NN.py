import numpy as np
from NNClasses import Neural_Network, Layer, Neuron

def printNeuronVals(layer):
    for neuron in layer:
        print(f"value: {neuron.value}, weight: {neuron.weight}, bias: {neuron.bias}")

def calculateNeuronVal(layer, currentNeuron):
    val = 0
    for neuron in layer:
        val += neuron.weight * neuron.value + currentNeuron.bias
    return val


def neuralNetwork(hiddenLayerLength, neuronsPerLayer, input):
    # init of the first layer
    firstLayer = Layer()
    hiddenLayers = []
    for i in range(len(input)):
        neuron = Neuron(np.random.rand(), 0, input[i])
        firstLayer.neurons.append(neuron)

    # setting hidden layers
    for i in range(hiddenLayerLength):
        layer = Layer()
        for j in range(neuronsPerLayer):
            neuron = Neuron(np.random.rand(), 0, 0)
            layer.neurons.append(neuron)
        hiddenLayers.append(layer)

    # forward propagation
    for i in range(len(hiddenLayers)):
        for neuron in hiddenLayers[i].neurons:
            if(not i):
                neuron.value = calculateNeuronVal(firstLayer.neurons, neuron)
            else:
                neuron.value = calculateNeuronVal(hiddenLayers[i - 1].neurons, neuron)
        
    for i in range(len(hiddenLayers)):
        print(f"Layer N: {i + 1}")
        printNeuronVals(hiddenLayers[i].neurons)
    
neuralNetwork(3, 4, [1, 2, 3, 4])