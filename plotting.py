import matplotlib.pyplot as plt

def Plot_Particles(f, x_points):
  ax = plt.subplot()

  y_points = [f(x) for x in x_points]

  X = []
  Y = []
  for i in range(1, 100):
    X.append(i / 10)
    Y.append(f([i / 10]))

  for i in range(len(x_points)):
    ax.scatter(x_points[i], y_points[i], marker='o', color='red')

  plt.plot(X, Y, label="f(x)")
  


  plt.xlabel("X-axis")
  plt.ylabel("Y-axis")
  plt.title(f"Plot of f(x) and Points")
  plt.grid(True) 
  plt.legend()
  plt.show()
