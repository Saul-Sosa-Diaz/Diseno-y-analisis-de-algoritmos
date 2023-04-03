"""
File: grasp.py
Author: Saúl Sosa Díaz
Date: 25/03/2023
Description: Implementation of the K-Means algorithm for solving a clustering problem.
This implementation generates random centroids and random assigns points to the cluster of the closest centroid.
Then, the centroids of each cluster are recalculated and the process is repeated until no further changes are made to the clusters.
"""

from algorithm import *
import random
from problem import Problem
import matplotlib.pyplot as plt
import colorsys


class GRASP(Algorithm):

  @typeguard.typechecked
  def __init__(self, problem: Problem, k: int = 3, cardinality: int = 3) -> None:
    '''
    This function initializes the Class GRASP.
    @param {Problem} problem - The problem to be solved.
    @param {int} [k=3] - The number of clusters to create.
    @param {int} [cardinality=3] - The number of items in each subset.
    '''
    if k > problem.GetNumOfPoints():
        raise Exception(bcolors.FAIL +
                        "Error in GRASP -> The number of clusters cannot exceed the number of points." + bcolors.ENDC +
                        "\nNumber of clusters: " + str(k) + "\nNumber of points in the problem: " + str(problem.GetNumOfPoints()))
    self.__problem = problem
    self.__k = k
    self.__cardinality = cardinality
    


  def ShowPlot(self, clusters, servicePoints, points):
    """
    It takes a list of clusters, a list of service points, and a list of all points. It then generates
    a random color for each cluster, and plots the points in each cluster with the corresponding color.
    It also plots the service points with the same color as the cluster they belong to
    @param clusters - A list of lists of points. Each list of points is a cluster.
    @param servicePoints - The points that are selected as service points.
    @param points - The list of points to be clustered
    """
    # Generate enough colors
    colors = []
    n = len(clusters)
    hue_values = [i/n for i in range(n)]
    random.shuffle(hue_values)
    for hue in hue_values:
        saturation = random.uniform(0.5, 1.0)
        value = random.uniform(0.5, 1.0)
        rgb = colorsys.hsv_to_rgb(hue, saturation, value)
        colors.append(rgb)
   
    # Order in which the dots were added to the clusters
    j = 0
    for point in points:
        plt.text(point[0], point[1] + 0.5, str(j),
                fontsize=12, ha='center', va='center')
        j += 1
    # Create a scatter plot for each set of points
    for i, point in enumerate(clusters):
        x = [p[0] for p in point]
        y = [p[1] for p in point]
        plt.scatter(x, y, color=colors[i] )
        
    # Show service points
    for color,i in enumerate(servicePoints):
      plt.scatter(self.__problem.GetPoints()[i][0], self.__problem.GetPoints()[i][1], s=100, color=colors[color], marker='*')
    # Show the graph
    plt.show()



  def GeneratePointsOfServices(self, points):
    """
    The function generates a random service point, then it calculates the distance between the service
    point and the rest of the points, then it selects the points with the highest distance and chooses
    one of them randomly
    @param points - The points that are to be considered for the solution.
    @returns The service points are returned.
    """
    servicePoints = []
    # Generate first random service point
    servicePoints.append(random.randint(0, self.__problem.GetNumOfPoints() - 1))
    # K service points are generated, we subtract 1 because one has been chosen at random and is already within the solution.
    for i in range(0, self.__k - 1):
      distances = []
      dict = {}
      for k, point in enumerate(points):
        value = 0
        for j in range(0, len(servicePoints)):
          value += self.EuclideanDistance(point, points[servicePoints[j]])

        # Do not choose again a service point that you have already chosen.
        if (k in servicePoints):
          value = -1

        distances.append(value)
        pointIndex = k
        dict[value] = pointIndex
        
      # Filter out the points that have already been included in the solution
      distances = [x for x in distances if x != -1]
      # The CRL is created with the cardinality indicated by the user and an element is randomly selected.
      lcr = sorted(distances)[-self.__cardinality:]
      randomElection = random.choice(lcr)
      servicePoints.append(dict[randomElection])

    return servicePoints
  


  def Solve(self):
    
    startTime = time.perf_counter()
    points = self.__problem.GetPoints().copy()

    servicePoints = self.GeneratePointsOfServices(points)
    
    print(servicePoints)

    # Eliminar los puntos de servicio
    points = np.delete(points, servicePoints, axis=0)

    # Crear los clusters y agregar los puntos de servicio a ellos
    clusters = [[]for i in range(0, self.__k)]
    for index, indexPoints in enumerate(servicePoints):
      clusters[index].append(self.__problem.GetPoints()[indexPoints]) 

    # permutación de los índices de la lista original
    indices = np.random.permutation(len(points))
    # evitar que los puntos se inspeccionen siempre en el mismo orden
    points = points[indices]
    
    # Por cada punto mirar que cluster tiene más cerca
    for point in points:
      indexAddToCluster = 0 # Es el indice del cluster que tiene menor distancia
      distMin = float('inf') # Es la distancia del cluster que tiene más cerca
      # Calcular el punto del cluster que está más cerca
      for index,cluster in enumerate(clusters):
        # Es la minima distancia del punto al punto que tiene mas cerca del cluster
        localMin = float('inf')
        for pointInCluster in cluster:
          value = self.EuclideanDistance(point, pointInCluster)
          if (localMin > value):
            localMin = value
        if (distMin > localMin):
          distMin = localMin
          indexAddToCluster = index
      # Añadir el punto al cluster más cercano
      clusters[indexAddToCluster].append(point)

    print(self.P_Median(clusters))
    self.ShowPlot(clusters, servicePoints, points)
    endTime = time.perf_counter()
    return (endTime - startTime)




def test():
  try:
    problem = Problem(
        r"E:\Cosas\universidad\tercero\Diseno-y-analisis-de-algoritmos\Practica7\problems\prob1.txt")
    a = GRASP(problem, 3)
    a.Solve()

  except Exception as e:
    print(str(e))


if __name__ == "__main__":
  test()
