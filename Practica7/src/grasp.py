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
    


  def ShowPlot(self, clusters, servicePoints):
    colores = []
    for i in range(len(clusters)):
        r = random.random()
        g = random.random()
        b = random.random()
        colores.append((r, g, b))
    # Crear un gráfico de dispersión para cada conjunto de puntos
    for i, puntos in enumerate(clusters):
        x = [p[0] for p in puntos]
        y = [p[1] for p in puntos]
        plt.scatter(x, y, color=colores[i])
    
    for color,i in enumerate(servicePoints):
      plt.scatter(self.__problem.GetPoints()[i][0], self.__problem.GetPoints()[i][1], s=100, color=colores[color], marker='*')
    # Mostrar el gráfico
    plt.show()



  def Solve(self):
    '''

    '''
    
    startTime = time.perf_counter()
    servicePoints = []
    # Generate first random service point
    servicePoints.append(random.randint(0, self.__problem.GetNumOfPoints() - 1))
    points = self.__problem.GetPoints().copy()
    for i in range(0,self.__k - 1): # se le resta uno porque ya se ha metido inicialmente el aleatorio.
      distances = []
      dict = {}
      for k, point in enumerate(points):
        value = 0
        for j in range(0, len(servicePoints)):
          value += self.EuclideanDistance(point, points[servicePoints[j]])
  
        if (k in servicePoints):
          value = -1
        distances.append(value)
        pointIndex = k
        dict[value] = pointIndex
        # The CRL is created with the cardinality indicated by the user and an element is randomly selected. 
      
      distances = [x for x in distances if x != -1]
      lcr = sorted(distances)[-self.__cardinality:]
      randomElection = random.choice(lcr)
      servicePoints.append(dict[randomElection])

    print(servicePoints)

    # Ahora asignamos a cada punto de servicio sus puntos más cercanos.
    points = self.__problem.GetPoints().view() #Hacer una copia
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

    self.ShowPlot(clusters, servicePoints)
    endTime = time.perf_counter()
    return (endTime - startTime)




def test():
  try:
    problem = Problem(
        r"E:\Cosas\universidad\tercero\Diseno-y-analisis-de-algoritmos\Practica7\problems\prob1.txt")
    a = GRASP(problem, 4)
    a.Solve()

  except Exception as e:
    print(str(e))


if __name__ == "__main__":
  test()
