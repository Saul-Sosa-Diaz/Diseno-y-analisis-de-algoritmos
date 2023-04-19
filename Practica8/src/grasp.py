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
    plt.scatter(centroid[0], centroid[1], color= "red")    
    # Show service points
    for i in servicePoints:
      plt.scatter(self.__problem.GetPoints()[i][0], self.__problem.GetPoints()[i][1], s=100, marker='*')
    # Show the graph
    plt.show()



  def FarestToCentroid(self, centroid, points):
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
      self.ShowPlot(solution, self.__problem.GetPoints(), centroid)
      centroid = self.CalculateCentroid(pointInSolution)
      newPoint = self.FarestToCentroid(centroid, points)
      solution.append(newPoint)
      points[newPoint] = float('inf')
      

    return solution


  def Grasp(self):
    """
    The Grasp function performs a constructive and improvement phase to find a solution to a problem,
    and returns the solution, pmedian, and the time taken to execute the function.
    @returns a list containing the solution, pmedian, and the time taken to execute the function.
    """
    startTime = time.perf_counter()

    # Constructive phase
    points = self.__problem.GetPoints()
    solution = self.GetSolution()
    print(solution)
    self.ShowPlot(solution, points, (-float('inf'), -float('inf')))
    # Improvement phase

    endTime = time.perf_counter()

    return self.__solution, round(self.__objetiveValue, 2), (endTime - startTime)


def test():
  try:
    problem = Problem(os.path.join(".", "problems", "max_div_15_2.txt"))
    a = GRASP(problem, 5, 1)
    
    print(a.Grasp())

  except Exception as e:
    print(str(e))


if __name__ == "__main__":
  test()
