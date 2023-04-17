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
    """
    This function initializes a GRASP algorithm with a given problem, number of clusters, and
    cardinality.
    @param {Problem} problem - an instance of the Problem class, which represents a clustering problem
    with a set of points and their distances.
    @param {int} [k=3] - The number of clusters to be formed in the problem.
    @param {int} [cardinality=3] - The cardinality parameter represents the maximum number of
    candidates that will be considered for each iteration of the GRASP algorithm. In other words, it
    limits the number of solutions that will be generated and evaluated at each iteration.
    """
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
        if j == 12:
          plt.text(point[0], point[1] - 0.5, str(j),
                   fontsize=12, ha='center', va='center')
        else:
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
    """
    This function takes a point as input and returns its corresponding index from a point dictionary.
    @param point - The parameter "point" is a variable that represents a point in a coordinate system.
    @returns The function `IndexTraductor` is returning yhe index of the point.
    """
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
    P_Median value and penalty factor, in this case 12, and multiplied by the number of elements in the cluster.
    @param clusters - The "clusters" parameter is a list of lists, where each inner list represents a
    cluster of data points. The objective function is being calculated for these clusters.
    @returns a value that is the sum of the result of the P_Median function applied to the clusters
    parameter and 12 times the length of the clusters parameter.
    """
    value = self.P_Median(clusters) + 10 * len(clusters)
    return value


  def CreateClusters(self, points, servicePoints):
    """
    The function creates clusters of points and adds service points to them, then assigns each
    non-service point to the closest cluster based on Euclidean distance.
    @param points - a list of points (coordinates) that need to be clustered
    @param servicePoints - A list of indices representing the points that are designated as service
    points. These points will be used as the initial centers of the clusters.
    @returns a list of clusters, where each cluster is a list of points.
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

    
  def CreateClustersInsert(self, clusters, newSolution):
    clustersCopy = copy.deepcopy(clusters)
    IndiceNuevoPunto = newSolution[-1]
    nuevoPunto = self.__problem.GetPoints()[IndiceNuevoPunto]
    newClusters = [[nuevoPunto]]
    
    for i, cluster in enumerate(clustersCopy):
      nuevoCluster = []
      for  punto in cluster:
        if self.IndexTraductor(punto) == IndiceNuevoPunto:
          pass
        elif self.__distanceMatrix[self.IndexTraductor(punto)][self.IndexTraductor(cluster[0])] > self.__distanceMatrix[self.IndexTraductor(punto)][IndiceNuevoPunto] and self.IndexTraductor(punto) not in newSolution:
          newClusters[-1].append(punto)
        else:
          nuevoCluster.append(punto)

      newClusters.insert(i, nuevoCluster)
    
    return newClusters

  def SearchInsert(self, solution):
    """
    This function searches for the best insertion point in a solution to improve its objective value.
    @param solution - A list representing the current solution to the problem. Each element in the list
    represents the index of a point in the problem instance.
    @returns the solution with the minimum objective value after performing a search and insert
    operation.
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
      NewClusters = self.CreateClustersInsert(clusters, baseSolution)
      objetiveValue = self.ObjetiveFunction(NewClusters)
      if objetiveValue < bestObjetiveValue:
        min = copy.deepcopy(baseSolution)
        bestObjetiveValue = objetiveValue

      baseSolution.pop()

    self.UpdateSolution(min, bestObjetiveValue) 
    return min



  def CreateClustersDelete(self, clusters, solution, newSolution):
    """
    This function creates clusters by deleting a solution from a set of clusters and adding its orphaned
    points to the nearest cluster.
    @param clusters - a list of clusters, where each cluster is represented as a list of points
    @param solution - It is a list representing the current solution, where each element represents the
    cluster to which a point belongs.
    @param newSolution - It is a list representing a new solution to a problem.
    @returns the updated clusters after removing a cluster and reassigning its orphaned points to the
    nearest cluster.
    """
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
    This function searches for and deletes a point of service from a solution, and returns the updated
    solution with the best objective value.
    @param solution - A list representing the current solution, where each element is a point of
    service.
    @returns the updated solution after performing a search and delete operation on the input solution.
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
    The function performs a search and swap operation to improve a given solution for a clustering
    problem.
    @param solution - The current solution to be improved by the search and swap algorithm.
    @returns the updated solution after performing a search and swap operation.
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
    """
    The function "Shaking" takes a solution and a number k, and returns a modified version of the
    solution by randomly swapping some of its elements with unused elements.
    @param solution - A list representing a solution to a problem, where each element is an index
    representing a point in the problem.
    @param k - The number of times the solution will be shaken or perturbed.
    @returns The function `Shaking` is returning a modified copy of the input `solution` list, where `k`
    random swaps have been made between the elements of the list.
    """
    solution_copy = solution.copy()
    posibles = set(range(0, self.__problem.GetNumOfPoints()))
    for i in range(0, k):
      for j in range(0, i):
          no_usados = posibles.difference(solution_copy)
          solution_copy[j] = random.choice(list(no_usados))
    
    return solution_copy



  def Search(self, solution):
    """
    The function performs a local search algorithm by iteratively applying swap, insert, and delete
    operations on a given solution until no improvement is made.
    The search operations alter the internal state of the machine.
    @param solution - The current solution that is being searched for improvement. It is likely a list
    or array of values that represent a solution to a problem.
    """
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
    """
    The GVNS function implements the General Variable Neighborhood Search algorithm to find a local optimal
    solution for a given problem.
    """
    startTime = time.perf_counter()
    k = 1
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
        k = 1
    
    actualSolution = bestSolution
    actualObjetiveValue
    self.UpdateSolution(actualSolution, actualObjetiveValue)
    endTime = time.perf_counter()
    
    return actualSolution, round(self.__objetiveValue, 2), (endTime - startTime), self.__k


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
    
    # Improvement phase
    self.SearchSwap(servicePointsIndex)

    endTime = time.perf_counter()

    return self.__solution, round(self.__objetiveValue, 2), (endTime - startTime)


def test():
  try:
    problem = Problem(os.path.join(".", "problems", "prob1.txt"))
    a = GRASP(problem, 5)
    
    print(a.Grasp())

  except Exception as e:
    print(str(e))


if __name__ == "__main__":
  test()
