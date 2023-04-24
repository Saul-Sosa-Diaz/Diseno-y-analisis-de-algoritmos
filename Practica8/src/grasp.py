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
import copy
import os


class GRASP(Algorithm):

  @typeguard.typechecked
  def __init__(self, problem: Problem, m: int = 3, cardinality: int = 3) -> None:
    """
    This function initializes a GRASP algorithm with a given problem, number of clusters, and
    cardinality.
    @param {Problem} problem - an instance of the Problem class, which represents a clustering problem
    with a set of points and their distances.
    @param {int} [m=3] - The number of points of diversity.
    @param {int} [cardinality=3] - The cardinality parameter represents the maximum number of
    candidates that will be considered for each iteration of the GRASP algorithm. In other words, it
    limits the number of solutions that will be generated and evaluated at each iteration.
    """
    if m > problem.GetNumOfPoints():
        raise Exception(bcolors.FAIL +
                        "Error in GRASP -> The points of diversity cannot exceed the number of points." + bcolors.ENDC +
                        "\nPoints of diversity: " + str(m) + "\nNumber of points in the problem: " + str(problem.GetNumOfPoints()))
    self.__problem = problem
    self.__m = m
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
          row.append(self.EuclideanDistance(points[i], points[j]))
      self.__distanceMatrix.append(row)

    self.__pointDictionary = {}
    for i, point in enumerate(points):
      self.__pointDictionary[str(point)] = i


  def IndexTraductor(self, point):
    """
    This function takes a point as input and returns its corresponding index from a point dictionary.
    @param point - The parameter "point" is a variable that represents a point in a coordinate system.
    @returns The function `IndexTraductor` is returning yhe index of the point.
    """
    return self.__pointDictionary[str(point)]
  


  def ShowPlot(self, servicePoints, points, centroid):
    """
    It takes a list of clusters, a list of service points, and a list of all points. It then generates
    a random color for each cluster, and plots the points in each cluster with the corresponding color.
    It also plots the service points with the same color as the cluster they belong to
    @param clusters - A list of lists of points. Each list of points is a cluster.
    @param servicePoints - The points that are selected as service points.
    @param points - The list of points to be clustered
    """
  
    # Order in which the dots were added to the clusters
    j = 0
    for point in points:
        plt.text(point[0], point[1] + 0.5, str(j),fontsize=12, ha='center', va='center')
        plt.scatter(point[0], point[1], s= 20 ,color="black")
        j += 1
    
    # Show service points
    for i in servicePoints[:-1]:
      plt.scatter(self.__problem.GetPoints()[i][0], self.__problem.GetPoints()[i][1], s=100, color="black", marker='*')
    
    plt.scatter(self.__problem.GetPoints()[servicePoints[-1]][0], self.__problem.GetPoints()[
                servicePoints[-1]][1], s=100, color="green", marker='*')
    plt.scatter(centroid[0], centroid[1], color="red")
    # Show the graph
    plt.show()



  def ObjetiveFunction(self, solution):
    '''This function calculates the objective value of a given solution based on a distance matrix.
    
    Parameters
    ----------
    solution
      A list representing a possible solution to a problem, where each element in the list represents a
    node or a city in a traveling salesman problem, for example. The objective function calculates the
    total distance or cost of visiting all the nodes in the given order. The distance between two nodes
    is obtained from a distance
    
    Returns
    -------
      the objective value of a given solution, which is calculated by summing the distances between all
    pairs of cities in the solution.
    
    '''
    objetiveValue = 0
    for i in range(0, len(solution)):
      for j in range(i + 1, len(solution)):
        objetiveValue += self.__distanceMatrix[solution[i]][solution[j]]
    return objetiveValue



  def FarestToCentroid(self, centroid, points):
    '''This function calculates the Euclidean distance between a centroid and a set of points, selects the
    farthest points from the centroid, and returns the index of the farthest point.
    
    Parameters
    ----------
    centroid
      The centroid is a point in the dataset that represents the center of a cluster. It is calculated as
    the mean of all the points in the cluster.
    points
      a list of points (as numpy arrays) for which we want to find the point farthest from the given
    centroid.
    
    Returns
    -------
      the index of the point in the "points" list that is farthest from the given centroid.
    
    '''
    distances = []
    DistAndPoints = {}
    for point in points:
      if not np.isinf(point).any():
        dist = self.EuclideanDistance(point, centroid)
        distances.append(dist)
        DistAndPoints[dist] = point
      
    #LRC
    distances = sorted(distances)[-self.__cardinality:]
    election = random.choice(distances)
    newpoint = DistAndPoints[election]
    
    return self.IndexTraductor(newpoint)
    


  def GetSolution(self):
    solution = []
    points = copy.deepcopy(self.__problem.GetPoints())
    POINTS = copy.deepcopy(self.__problem.GetPoints())
    centroid = self.CalculateCentroid(points)
    solution.append(self.FarestToCentroid(centroid, points))
    points[solution[0]] = float('inf')
    for i in range(0, self.__m - 1):
      pointInSolution = [POINTS[j] for j in solution]
      #self.ShowPlot(solution, self.__problem.GetPoints(), centroid)
      centroid = self.CalculateCentroid(pointInSolution)
      newPoint = self.FarestToCentroid(centroid, points)
      solution.append(newPoint)
      points[newPoint] = float('inf')
      
    return solution


  def ObjetiveFuntionFromSolution(self, actualObtetiveValue, newElement, oldElement, solution):
    '''This function calculates the objective function value by subtracting the distance between oldElement
    and each point in the solution and adding the distance between newElement and each point in the
    solution.
    
    Parameters
    ----------
    actualObtetiveValue
      The current value of the objective function before considering the new element.
    newElement
      The new element is a point that is being added to the solution. It is used to calculate the change
    in the objective function value when this point is added to the solution.
    oldElement
      The index of the element that is being replaced in the solution with a new element.
    solution
      A list of indices representing the current solution or path.
    
    Returns
    -------
      the updated objective function.
    '''
    distSubtract = 0
    distSum = 0
    for indexPoint in solution:
      distSubtract += self.__distanceMatrix[oldElement][indexPoint]
      distSum += self.__distanceMatrix[newElement][indexPoint]
    
    return actualObtetiveValue - distSubtract + distSum
  


  def tabuSearch(self, solution, iter, numberTabu):
    numberTabu += 1
    newSolution = copy.deepcopy(solution)
    max = None
    playgroundSet = [i for i in range(0, self.__problem.GetNumOfPoints())]
    actualObjetiveValue = self.ObjetiveFunction(newSolution)
    maxObjetiveValue = -float('inf')
    tabuTable = np.zeros((self.__problem.GetNumOfPoints(), self.__problem.GetNumOfPoints()))
    
    for j in range(0,self.__problem.GetNumOfPoints()):
      tabuTable[j,j] = float('inf')
    
    i = 0
    while i < iter:
      intercambio = {}
      for k in range(0, self.__problem.GetNumOfPoints()):
        for h in range(k, self.__problem.GetNumOfPoints()):
          if tabuTable[k][h] != 0 and tabuTable[k][h] != float('inf'):
            tabuTable[k][h] -= 1

      playground = list(set(playgroundSet) - set(newSolution))
      for element in playground:
        for indexOfPoint, point in enumerate(newSolution):
          point = newSolution.pop(indexOfPoint)
          # Operacion
          if newSolution != solution:
            objetiveValue = self.ObjetiveFuntionFromSolution(actualObjetiveValue, element, point, newSolution)
            intercambio[objetiveValue] = [point, element]

          newSolution.insert(indexOfPoint, point)
      ordenado = sorted(intercambio.keys(), reverse = True )
      
      j = 0
      while j < len(ordenado):

        # Criterio de aspiración
        if ordenado[j] > maxObjetiveValue:
          if intercambio[ordenado[j]][0] < intercambio[ordenado[j]][1]:
            tabuTable[intercambio[ordenado[j]][0]][intercambio[ordenado[j]][1]] = numberTabu
          else: 
            tabuTable[intercambio[ordenado[j]][1]][intercambio[ordenado[j]][0]] = numberTabu 
          maxObjetiveValue = ordenado[j]
          actualObjetiveValue = maxObjetiveValue
          for i in range(len(newSolution)):
            if newSolution[i] == intercambio[ordenado[j]][0]:
              newSolution[i] = intercambio[ordenado[j]][1]
              max = copy.deepcopy(newSolution)
              break
          break

        # Elegir uno que no sea tabú
        elif tabuTable[intercambio[ordenado[j]][0]][intercambio[ordenado[j]][1]] == 0:
          if intercambio[ordenado[j]][0] < intercambio[ordenado[j]][1]:
            tabuTable[intercambio[ordenado[j]][0]][intercambio[ordenado[j]][1]] = numberTabu
          else: 
            tabuTable[intercambio[ordenado[j]][1]][intercambio[ordenado[j]][0]] = numberTabu 

          actualObjetiveValue = ordenado[j]
          for w in range(len(newSolution)):
            if newSolution[w] == intercambio[ordenado[j]][0]:
              newSolution[w] = intercambio[ordenado[j]][1]
              break
          break

        j += 1
      i += 1

    return max, maxObjetiveValue



  def SearchSwap(self, solution, objetiveValue):
    """
    The function performs a search and swap operation to improve a given solution for a clustering
    problem.
    @param solution - The current solution to be improved by the search and swap algorithm.
    @returns the updated solution after performing a search and swap operation.
    """

    newSolution = copy.deepcopy(solution)
    max = None
    playgroundSet = [i for i in range(0, self.__problem.GetNumOfPoints())]
    bestObjetiveValue = objetiveValue
    MaxObjetiveValue = None

    while True:
      playground = list(set(playgroundSet) - set(newSolution))
      for element in playground:
        for indexOfPoint, point in enumerate(newSolution):
          point = newSolution.pop(indexOfPoint)
          # Operacion
          if newSolution != solution:
            objetiveValue = self.ObjetiveFuntionFromSolution(bestObjetiveValue, element, point, newSolution)
            if bestObjetiveValue < objetiveValue:
              max = copy.deepcopy(newSolution)
              max.insert(indexOfPoint, element)
              MaxObjetiveValue = objetiveValue

          newSolution.insert(indexOfPoint, point)
      
      if max == newSolution or max == None:
        bestObjetiveValue = MaxObjetiveValue
        break
      newSolution = max
      bestObjetiveValue = MaxObjetiveValue
  
    return max, bestObjetiveValue

  def Grasp(self, iter):
    startTime = time.perf_counter()
    bestSolution = None
    bestObjetiveValue = -float('inf')
    iterWithOutUpgrade = 0
    i = 0

    while i <= iter and iterWithOutUpgrade < 100:
      # Constructive phase
      solution = self.GetSolution()
      actualObjetiveValue = self.ObjetiveFunction(solution)
      #points = self.__problem.GetPoints()
      #self.ShowPlot(solution, points, (-float('inf'), -float('inf')))
      
      # Improvement phase
      if self.__cardinality != 1 :
        actualSolution, objetiveValue = self.SearchSwap(solution, actualObjetiveValue)
        if actualSolution != None:
          solution = actualSolution
          actualObjetiveValue = objetiveValue

      iterWithOutUpgrade += 1
      i += 1
      # Update solution
      if bestObjetiveValue < actualObjetiveValue:
        bestSolution = solution
        bestObjetiveValue = actualObjetiveValue
        iterWithOutUpgrade = 0
      
    endTime = time.perf_counter()
    return bestSolution, round(bestObjetiveValue, 2), round((endTime - startTime), 7)


def test():
  try:
    problem = Problem(os.path.join(".", "problems", "max_div_15_2.txt"))
    
    # Greedy
    a = GRASP(problem, 3, 1)
    
    # Grasp
    g = GRASP(problem, 3, 40)
    print(bcolors.UNDERLINE + "Greedy" + bcolors.ENDC)
    print(a.Grasp(1))
    print(bcolors.UNDERLINE + "Grasp" + bcolors.ENDC)
    print(g.Grasp(400))
   
    #print(a.tabuSearch([0,4,3], 5, 3))

  except Exception as e:
    print(str(e))


if __name__ == "__main__":
  test()
