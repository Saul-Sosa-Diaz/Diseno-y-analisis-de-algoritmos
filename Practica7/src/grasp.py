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
import numpy as np


class GRASP(Algorithm):

  @typeguard.typechecked
  def __init__(self, problem: Problem, k: int = 3, cardinality: int = 3) -> None:
    '''
    This function initializes the Class GRASP.
    @param {Problem} problem - The problem to be solved.
    @param {int} [k=3] - The number of clusters to create.
    @param {int} [cardinality=3] - The number of items in each subset.
    '''
    self.__problem = problem
    self.__k = k
    self.__cardinality = cardinality

  def Solve(self):
    '''
    The function generates random centroids, then it calculates the distance from each point to each
    centroid, then it creates a CRL with the cardinality indicated by the user and an element is
    randomly selected. Then, the new centroids are calculated and the SSE is returned
    @returns The SSE and the time it took to run the algorithm.
    '''
    
    
    startTime = time.perf_counter()
    # Generate aleatory centroids
    centroids = random.sample(
        range(0, self.__problem.GetNumOfPoints()), self.__k)
    aux = []
    for i in centroids:
      aux.append(self.__problem.GetPoints()[i])
    centroids = aux

    # Empty solution
    cluster = []
    newClusters = [[]for i in range(0, self.__k)]
    newCentroids = []

    while True:
      # Reset the new cluters
      newCentroids.clear()
      for i in range(self.__k):
        newClusters[i] = []

      for j in range(0, self.__problem.GetNumOfPoints()):
        mins = []
        # The distance from this point to all clusters is stored.
        dict = {}  
        # The distance to each cluster is calculated
        for i, centroid in enumerate(centroids):
          value = self.EuclideanDistance(self.__problem.GetPoints()[j], centroid)
          mins.append(value)
          CentroidIndex = i
          dict[value] = CentroidIndex

        # The CRL is created with the cardinality indicated by the user and an element is randomly selected.
        mins = sorted(mins)[:self.__cardinality]

        random_election = random.choice(mins)

        newClusters[dict[random_election]].append(
          self.__problem.GetPoints()[j])

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
    a = GRASP(problem, 4)
    a.Solve()

  except Exception as e:
    print(str(e))


if __name__ == "__main__":
  test()
