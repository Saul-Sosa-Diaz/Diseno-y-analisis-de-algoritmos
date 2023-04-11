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
import os


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

    # For each point look at which cluster is closer
    for index,point in enumerate(points):
      if index in servicePoints:
        continue
      
      # Calculate the cluster that is closest to the actual point.
      min = float('inf')
      clusterIndex = 0
      for index, pointOfService in enumerate(servicePoints):
        value = self.EuclideanDistance(point, points[pointOfService])
        if (min > value):
          min = value
          clusterIndex = index

      # Add the point to the nearest cluster
      clusters[clusterIndex].append(point)
    
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
    # Generate a random point.
    servicePoints.append(random.randint(0, self.__problem.GetNumOfPoints() - 1))
    for i in range(0, self.__k - 1):
      dict = {}
      distances = []
      # The distance from each point to the solution is calculated.
      for index, point in enumerate(points):
        # The distance from a point to a set is the smallest distance.
        minDistance = float('inf')
        value = float('inf')
        if index not in servicePoints:
          for servicePoint in servicePoints:
              value = self.EuclideanDistance(point,  points[servicePoint])
              if (minDistance > value):
                minDistance = value
          distances.append(minDistance)
          dict[minDistance] = index
      
      # The list of candidates is calculated and one is chosen at random.
      lcr = sorted(distances)[-self.__cardinality:]
      randomElection = random.choice(lcr)
      servicePoints.append(dict[randomElection])

    return servicePoints
  


  def Grasp(self):
    """
    The Grasp function performs a constructive and improvement phase to find a solution to a problem,
    and returns the solution, pmedian, and the time taken to execute the function.
    @returns a list containing the solution, pmedian, and the time taken to execute the function.
    """
    startTime = time.perf_counter()

    # Constructive phase
    points = self.__problem.GetPoints()
    servicePointsIndex = self.GeneratePointsOfServices(points)
    clusters = self.CreateClusters(points, servicePointsIndex)
    self.ShowPlot(clusters,servicePointsIndex,points)
    self.__solution = servicePointsIndex
    self.__pmedian = self.P_Median(clusters)

    # Improvement phase
    self.SearchSwap()

    endTime = time.perf_counter()
    servicePoints = [list(self.__problem.GetPoints()[i]) for i in self.__solution]
    

    return servicePoints , round(self.__pmedian,2), (endTime - startTime)



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
    problem = Problem(os.path.join(".", "problems", "prob1.txt"))
    a = GRASP(problem, 3)
    
    print(a.Grasp())

  except Exception as e:
    print(str(e))


if __name__ == "__main__":
  test()
