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
import copy
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
    self.__objetiveValue = None
    self.__solution = None
    points = problem.GetPoints()
    self.__distanceMatrix = []
    for i in range(0, len(points)):
      row = []
      for j in range(0, len(points)):
        if j == i:
          row.append(float('inf'))
        elif j < i:
          row.append(self.EuclideanDistance(points[j], points[i]))
        else:
          row.append(self.EuclideanDistance(points[i],points[j]))
      self.__distanceMatrix.append(row)
    
    self.__pointDictionary = {}
    for i, point in enumerate(points):
      self.__pointDictionary[str(point)] = i



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
  
  

  def IndexTraductor(self, point):
    return self.__pointDictionary[str(point)]



  def UpdateSolution(self, servicePoints, objetiveValue):
    """
    This function updates the solution and objective value of a given problem instance.
    @param servicePoints - It is a list or array that represents the updated solution for a given
    problem. In the context of this code snippet, it is likely that the problem involves finding the
    optimal locations for service points or facilities.
    @param objetiveValue - The objective value is a numerical value that represents the quality or
    effectiveness of the solution. In the context of this code, it likely represents the total
    distance or cost of the solution. The lower the objective value, the better the solution.
    """
    self.__solution = servicePoints
    self.__objetiveValue = objetiveValue
    self.__k = len(servicePoints)




  def ObjetiveFunction(self, clusters):
    """
    This function calculates the objective function value for a given set of clusters by adding the
    P_Median value and penalty factor, in this case 10, and multiplied by the number of elements in the cluster.
    @param clusters - The "clusters" parameter is a list of lists, where each inner list represents a
    cluster of data points. The objective function is being calculated for these clusters.
    @returns a value that is the sum of the result of the P_Median function applied to the clusters
    parameter and 10 times the length of the clusters parameter.
    """
    value = self.P_Median(clusters) + 5 * len(clusters)
    return value


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
    for index, point in enumerate(points):
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
      for indexPoint, point in enumerate(points):
        # The distance from a point to a set is the smallest distance.
        minDistance = float('inf')
        value = float('inf')
        if indexPoint not in servicePoints:
          for servicePoint in servicePoints:
              value = self.__distanceMatrix[indexPoint][servicePoint]
              if (minDistance > value):
                minDistance = value
          distances.append(minDistance)
          dict[minDistance] = indexPoint
      
      # The list of candidates is calculated and one is chosen at random.
      lcr = sorted(distances)[-self.__cardinality:]
      randomElection = random.choice(lcr)
      servicePoints.append(dict[randomElection])

    return servicePoints



  def SearchInsert(self, solution):
    """
    This function performs a search and insert algorithm to find the optimal solution for a p-median
    problem.
    Stop conditions are when the error is 0 or when the error is improved by less than 30%.
    """
    baseSolution = copy.deepcopy(solution)
    clusters = self.CreateClusters(self.__problem.GetPoints(), baseSolution)
    bestObjetiveValue = self.ObjetiveFunction(clusters)
    min = copy.deepcopy(baseSolution)
  
    i = 0
    playground = []
    while len(playground) + len(baseSolution) < self.__problem.GetNumOfPoints():
      if i not in baseSolution:
        playground.append(i)
      i += 1
   
    for element in playground:
      baseSolution.append(element)
      # Operacion
      clusters = self.CreateClusters(self.__problem.GetPoints(), baseSolution)
      objetiveValue = self.ObjetiveFunction(clusters)
      if objetiveValue < bestObjetiveValue:
        min = copy.deepcopy(baseSolution)
        bestObjetiveValue = objetiveValue

      baseSolution.pop()

    self.UpdateSolution(min, bestObjetiveValue) 
    return min



  def CreateClustersDelete(self, clusters, solution, newSolution):
    clusters = copy.deepcopy(clusters)
    faltantes = [indice for indice, numero in enumerate(solution) if numero not in newSolution]
    puntosHuerfanos = copy.deepcopy(clusters[faltantes[0]])
    clusters.pop(faltantes[0])
    for punto in puntosHuerfanos:
      minDist = float('inf')
      indexCluster = -1
      for index, cluster in enumerate(clusters):
        dist = self.__distanceMatrix[self.IndexTraductor(punto)][self.IndexTraductor(cluster[0])]
        if minDist > dist:
          minDist = dist
          indexCluster = index
          
      clusters[indexCluster].append(punto)
    return clusters



  def SearchDelete(self, solution):
    """
    This function searches for and deletes points of service from a solution, and updates the solution
    and pmedian accordingly.
    """ 
    newSolution = copy.deepcopy(solution)
    min = copy.deepcopy(newSolution)
    clusters = self.CreateClusters(self.__problem.GetPoints(), newSolution)
    bestObjetiveValue = self.ObjetiveFunction(clusters)
    if self.__k > 2:
      for indexOfSolution, pointOfService in enumerate(newSolution):
        pointOfService = newSolution.pop(indexOfSolution)
        # Operacion
        newClusters = self.CreateClustersDelete(clusters, solution, newSolution)
        objetiveValue = self.ObjetiveFunction(newClusters)
        if objetiveValue < bestObjetiveValue:
            min = copy.deepcopy(newSolution)
            bestObjetiveValue = objetiveValue

        newSolution.insert(indexOfSolution, pointOfService)
    
      self.UpdateSolution(min, bestObjetiveValue)

    return min



  def SearchSwap(self, solution):
    """
    The function SearchSwap implements a local search algorithm to improve a solution obtained by the
    GRASP algorithm by swapping facilities and searching for a better solution.
    """
    newSolution = copy.deepcopy(solution)
    min = copy.deepcopy(newSolution)
    playgroundSet = [i for i in range(0, self.__problem.GetNumOfPoints())]
    bestClusters = self.CreateClusters(self.__problem.GetPoints(), newSolution)
    bestObjetiveValue = self.ObjetiveFunction(bestClusters)

    while True:
      playground = list(set(playgroundSet) - set(newSolution))
      for element in playground:
        for indexOfSolution, pointOfService in enumerate(newSolution):
          pointOfService = newSolution.pop(indexOfSolution)
          newSolution.insert(indexOfSolution, element)
          # Operacion
          if newSolution != solution:
            clusters = self.CreateClusters(self.__problem.GetPoints(), newSolution)
            objetiveValue = self.ObjetiveFunction(clusters)
            if bestObjetiveValue > objetiveValue:
              min = copy.deepcopy(newSolution)
              bestObjetiveValue = objetiveValue
              bestClusters = clusters
          newSolution.pop(indexOfSolution)
          newSolution.insert(indexOfSolution, pointOfService)
      
      if min == newSolution:
        break
      newSolution = min
      clusters = bestClusters

    self.UpdateSolution(newSolution, bestObjetiveValue)  
    return newSolution



  def Shaking(self, solution, k):
    solution_copy = solution.copy()
    posibles = set(range(0, self.__problem.GetNumOfPoints()))
    for i in range(1, k - 1):
      for j in range(0, i):
          no_usados = posibles.difference(solution_copy)
          solution_copy[j] = random.choice(list(no_usados))
    
    return solution_copy



  def Search(self, solution):
    l = 0
    while l <= 2:
      if l == 0:
        solution = self.SearchSwap(solution) 
        objetiveValueAnterior = copy.deepcopy(self.__objetiveValue)
        l +=1
      elif l == 1:
        solution = self.SearchInsert(solution)
        if objetiveValueAnterior <= self.__objetiveValue:
          l += 1
        else:
          objetiveValueAnterior = copy.deepcopy(self.__objetiveValue)
          l = 0
      else:
        solution = self.SearchDelete(solution)
        if objetiveValueAnterior <= self.__objetiveValue:
          l += 1
        else:
          objetiveValueAnterior = copy.deepcopy(self.__objetiveValue)
          l = 0
    


  def GVNS(self):
    k = 0
    actualSolution = copy.deepcopy(self.__solution)
    bestSolution = copy.deepcopy(self.__solution)
    actualObjetiveValue = copy.deepcopy(self.__objetiveValue)
    while k <= self.__k:
      actualSolution = self.Shaking(actualSolution,k)
      self.Search(actualSolution)
      if actualObjetiveValue <= self.__objetiveValue:
        k += 1
      else: 
        bestSolution = copy.deepcopy(self.__solution)
        actualSolution = copy.deepcopy(self.__solution)
        actualObjetiveValue = copy.deepcopy(self.__objetiveValue)
        k = 0
    
    actualSolution = bestSolution
    actualObjetiveValue
    self.UpdateSolution(actualSolution, actualObjetiveValue)



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
    #print(servicePointsIndex)
    clusters = self.CreateClusters(points, servicePointsIndex)
    objetiveValue = self.ObjetiveFunction(clusters)
    self.UpdateSolution(servicePointsIndex, objetiveValue)
    
    # self.ShowPlot(clusters, servicePointsIndex, points)
    # Improvement phase
    self.GVNS()

    endTime = time.perf_counter()
    servicePoints = [list(self.__problem.GetPoints()[i])
                     for i in self.__solution]
    clusters = self.CreateClusters(points, self.__solution)
    
    #print(self.__solution)
    #print(self.ObjetiveFunction(self.CreateClusters(
    #    self.__problem.GetPoints(), self.__solution)))
    # self.ShowPlot(clusters, self.__solution, points)
    return servicePoints, round(self.__objetiveValue, 2), (endTime - startTime)


def test():
  try:
    problem = Problem(os.path.join(".", "problems", "prob2.txt"))
    a = GRASP(problem, 2)
    
    print(a.Grasp())

  except Exception as e:
    print(str(e))


if __name__ == "__main__":
  test()
