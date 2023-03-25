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


class GRASP(Algorithm):

  @typeguard.typechecked
  def __init__(self, problem: Problem, k: int = 3) -> None:
    self.__problem = problem
    self.__k = k

  def Solve(self):
    '''
    This function implements the K-Means algorithm for solving a clustering problem.

    In this implementation, random centroids are generated and points are assigned to the cluster of the closest centroid.
    Then, the centroids of each cluster are recalculated and the process is repeated until no further changes are made to the clusters.
    Finally, the length of each cluster is printed.
    '''

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
      for i in range(self.__k):
        newClusters[i] = []

      for j in range(0, self.__problem.GetNumOfPoints()):
        mins = []
        min = float('inf')
        minIndex = -1
        dict = {}
        # Se calcula la distancia a cada cluster
        for i, centroid in enumerate(centroids):
          value = self.EuclideanDistance(self.__problem.GetPoints()[j], centroid)
          mins.append(value)
          minIndex = i
          dict[value] = minIndex
            
        mins = sorted(mins)[:3]
        random_election = random.choice(mins)

        newClusters[dict[random_election]].append(
          self.__problem.GetPoints()[j])

      # New centroids are calculated
      for i in newClusters:
        newCentroids.append(self.CalculateCentroids(i))

      if newClusters == cluster:
        break
      else:
        cluster = newClusters
        centroids = newCentroids

    for i in range(0, self.__k):
      print("Cluster", i, "length:", len(cluster[i]))


def main():
  try:
    problem = Problem(
        r"E:\Cosas\universidad\tercero\Diseno-y-analisis-de-algoritmos\Practica7\problems\prob1.txt")
    a = GRASP(problem, 4)
    a.Solve()

  except Exception as e:
    print(str(e))


if __name__ == "__main__":
  main()
