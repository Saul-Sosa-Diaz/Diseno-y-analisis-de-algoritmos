"""
File: greedy.py
Author: Saúl Sosa Díaz
Date: 25/03/2023
Description: Implementation of the K-Means algorithm for solving a clustering problem.
This implementation generates random centroids and assigns points to the cluster of the closest centroid.
Then, the centroids of each cluster are recalculated and the process is repeated until no further changes are made to the clusters.
Finally, the length of each cluster is printed.
"""

from algorithm import *
import random 
from problem import Problem
import numpy as np

class Greedy(Algorithm):

  @typeguard.typechecked
  def __init__(self, problem : Problem, k : int = 3) -> None:
    '''
      Initializes a new instance of the Greedy class.

      Args:
          problem (Problem): An instance of the Problem class containing the data for the problem.
          k (int, optional): The number of clusters to create. Defaults to 3.

      Returns:
          None.
    '''
    self.__problem = problem
    self.__k = k
  


  def Solve(self):
    '''
    This function implements the K-Means algorithm for solving a clustering problem.

    In this implementation, random centroids are generated and points are assigned to the cluster of the closest centroid.
    Then, the centroids of each cluster are recalculated and the process is repeated until no further changes are made to the clusters.
    Finally, the length of each cluster is printed.
    '''

    startTime = time.perf_counter()
    # Generate aleatory centroids
    centroids = random.sample(range(0, self.__problem.GetNumOfPoints()), self.__k) 
    aux = []
    for i in centroids:
      aux.append(self.__problem.GetPoints()[i])
    centroids = aux
    
    # Empty solution
    cluster = []
    newClusters = [[]for i in range(0, self.__k)]  
    newCentroids = []

    while True:
      newCentroids.clear()
      # Reset the new cluters
      for i in range(self.__k):  
        newClusters[i] = []
      
      for j in range(0, self.__problem.GetNumOfPoints()):
        min = float('inf')
        minIndex = -1
        # For each point the centroids are traversed and pushed into the cluster of the centroid that is closest to it
        for i, centroid in enumerate(centroids):
          if min > self.EuclideanDistance(self.__problem.GetPoints()[j], centroid):
            minIndex = i
            min = self.EuclideanDistance(self.__problem.GetPoints()[j], centroid)
        newClusters[minIndex].append(self.__problem.GetPoints()[j])

      # New centroids are calculated
      for i in newClusters:
        newCentroids.append(self.CalculateCentroids(i))
      
      if newClusters == cluster:
        centroids = newCentroids
        break
      else:
        cluster = newClusters
        centroids = list(newCentroids)
        
    sse = self.SSE(cluster, centroids)

    endTime = time.perf_counter()
    return sse, (endTime - startTime)



def test():
  try:
    problem = Problem(
        r"E:\Cosas\universidad\tercero\Diseno-y-analisis-de-algoritmos\Practica7\problems\prob1.txt")
    a = Greedy(problem, 4)
    print(a.Solve())


  except Exception as e:
    print(str(e))


if __name__ == "__main__":
  test()


