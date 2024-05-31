import numpy as np
import matplotlib.pyplot as plt

def plotFct(data_x, data_y, f):

    # Generate grids for x and y values
    x = np.linspace(-10, 10, 100)
    y = np.linspace(-10, 10, 100)
    X, Y = np.meshgrid(x, y)

    # Calculate z values (f(x, y))
    Z = f([X, Y])

    # Create the contour plot
    plt.contour(X, Y, Z)

    # Plot the data points on top of the contour
    plt.scatter(data_x, data_y, color='red', marker='o', label='Data Points')

    # Add labels, title, and legend
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Contour Plot of f(x, y) with Data Points")
    plt.colorbar(label="f(x, y)")
    plt.legend()
    plt.show()
