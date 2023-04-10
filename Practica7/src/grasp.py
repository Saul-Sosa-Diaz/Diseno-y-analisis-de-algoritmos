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
    self.__pmedian = None
    self.__solution = None
    


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



  def CreateClusters(self, points, servicePoints):
    """
    It takes a list of points and a list of service points and returns a list of clusters
    @param points - the points to be clustered
    @param servicePoints - The points that are already in the clusters.
    @returns The clusters are being returned.
    """
    # Create the clusters and add the service points to them
    clusters = [[]for i in range(0, len(servicePoints))]
    for index, indexPoints in enumerate(servicePoints):
      clusters[index].append(self.__problem.GetPoints()[indexPoints])

    # Avoid always inspecting the points in the same order
    indices = np.random.permutation(len(points))
    points = points[indices]

    # For each point look at which cluster is closer
    for point in points:
      # It is the index of the cluster that has the smallest distance to the actual point
      indexAddToCluster = 0
      # It is the distance from the nearest cluster to the actual point
      distMin = float('inf')
      # Calculate the cluster that is closest to the actual point.
      for index, cluster in enumerate(clusters):
        localMin = float('inf')
        # Calculate the minimum distance from the point to all points in the cluster.
        for pointInCluster in cluster:
          value = self.EuclideanDistance(point, pointInCluster)
          if (localMin > value):
            localMin = value

        if (distMin > localMin):
          distMin = localMin
          indexAddToCluster = index

      # Add the point to the nearest cluster
      clusters[indexAddToCluster].append(point)
    
    return clusters



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
  


  def Grasp(self):
    """
    The function generates the service points, then it separates the service points from the demand
    points, then it creates the clusters and adds the service points to them, then it avoids always
    inspecting the points in the same order, then it calculates the cluster that is closest to the
    actual point, then it adds the point to the nearest cluster, then it returns the time it took to execute the algorithm.
    @returns time it took to execute the algorithm.
    """
    startTime = time.perf_counter()

    # Constructive phase
    points = self.__problem.GetPoints().copy()
    servicePoints = self.GeneratePointsOfServices(points)
    points = np.delete(points, servicePoints, axis=0)
    clusters = self.CreateClusters(points, servicePoints)
    self.__solution = servicePoints
    self.__pmedian = self.P_Median(clusters)

    # Improvement phase
    self.SearchSwap()

    endTime = time.perf_counter()
    return self.__solution,self.__pmedian,(endTime - startTime)



  def SearchInsert(self):
    """
    This function performs a search and insert algorithm to find the optimal solution for a p-median
    problem.
    Stop conditions are when the error is 0 or when the error is improved by less than 30%.
    """
    if not self.__solution:
      raise Exception(
          bcolors.FAIL + "Error in GRASP -> Solve has not yet been executed. No solution exists." + bcolors.ENDC)
 
    baseSolution = self.__solution
    minPmedian = self.__pmedian
    previousPmedian = float('inf')

    i = 0
    playground = []
    while len(playground) + len(baseSolution) < self.__problem.GetNumOfPoints():
      if i not in baseSolution:
        playground.append(i)

      i += 1

    while True:
      for element in playground:
        baseSolution.append(element)
        # Operacion
        clusters = self.CreateClusters(self.__problem.GetPoints(), baseSolution)
        pmedian = self.P_Median(clusters)
        if pmedian < minPmedian:
          min = baseSolution.copy()
          minPmedian = pmedian
        baseSolution.pop()

      if previousPmedian == 0 or (previousPmedian - minPmedian) / previousPmedian <= 0.3: # stopping criteria
        break

      baseSolution = min
      previousPmedian = minPmedian

    self.__pmedian = minPmedian
    self.__solution = min


  def SearchDelete(self):
    """
    This function searches for and deletes points of service from a solution, and updates the solution
    and pmedian accordingly.
    """
    if not self.__solution:
      raise Exception(
          bcolors.FAIL + "Error in GRASP -> Solve has not yet been executed. No solution exists." + bcolors.ENDC)
    
    baseSolution = self.__solution
    min = baseSolution.copy()
    minPmedian = self.__pmedian
    while True:
      for indexOfSolution, pointOfService in enumerate(baseSolution):
        pointOfService = baseSolution.pop(indexOfSolution)
        # Operacion
        clusters = self.CreateClusters(self.__problem.GetPoints(), baseSolution)
        pmedian = self.P_Median(clusters)
        if pmedian < minPmedian:
            min = baseSolution.copy()
            minPmedian = pmedian

        baseSolution.insert(indexOfSolution, pointOfService)

      if min == baseSolution:
        break
      baseSolution = min

    self.__pmedian = minPmedian
    self.__solution = baseSolution



  def SearchSwap(self):
    """
    The function SearchSwap implements a local search algorithm to improve a solution obtained by the
    GRASP algorithm by swapping facilities and searching for a better solution.
    """
    if not self.__solution:
      raise Exception(bcolors.FAIL + "Error in GRASP -> Solve has not yet been executed. No solution exists." + bcolors.ENDC)
    
    baseSolution = self.__solution
    min = baseSolution.copy()
    minPmedian = self.__pmedian
    playgroundSet = [i for i in range(0, self.__problem.GetNumOfPoints())]

    while True:
      playground = list(set(playgroundSet) - set(baseSolution))

      for element in playground:
        for indexOfSolution, pointOfService in enumerate(baseSolution):
          pointOfService = baseSolution.pop(indexOfSolution)
          baseSolution.insert(indexOfSolution, element)
          # Operacion
          clusters = self.CreateClusters(self.__problem.GetPoints(), baseSolution)
          pmedian = self.P_Median(clusters)
          if pmedian < minPmedian:
            min = baseSolution.copy()
            minPmedian = pmedian

          baseSolution.pop(indexOfSolution)
          baseSolution.insert(indexOfSolution, pointOfService)
      
      if min == baseSolution:
        break
      baseSolution = min

    self.__pmedian = minPmedian
    self.__solution = baseSolution




def test():
  try:
    problem = Problem(
        r"E:\Cosas\universidad\tercero\Diseno-y-analisis-de-algoritmos\Practica7\problems\prob1.txt")
    a = GRASP(problem, 3)
    print(a.Grasp())

  except Exception as e:
    print(str(e))


if __name__ == "__main__":
  test()
