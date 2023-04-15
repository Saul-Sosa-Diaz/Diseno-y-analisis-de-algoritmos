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
import matplotlib.pyplot as plt
import colorsys
import os

# This class implements the K-Means algorithm for solving a clustering problem
class Greedy(Algorithm):

  @typeguard.typechecked
  def __init__(self, problem : Problem, k : int = 3) -> None:
    '''
    This function initializes the Class Greedy.
    @param {Problem} problem - The problem to be solved.
    @param {int} [k=3] - The number of clusters to create.
    '''
    self.__problem = problem
    self.__k = k

  
  
  def ShowPlot(self, clusters, servicePoints):
    """
    It takes a list of clusters and a list of service points and plots them on a graph
    @param clusters - A list of lists of points. Each list of points represents a cluster.
    @param servicePoints - The list of service points.
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

    j = 0
    # Create a scatter plot for each set of points
    for i, point in enumerate(clusters):
        x = [p[0] for p in point]
        y = [p[1] for p in point]
        plt.scatter(x, y, color=colors[i])

    for color, i in enumerate(servicePoints):
      plt.scatter(i[0], i[1], s=100, color=colors[color], marker='*')
    # Show the graph
    plt.show()

  def P_Median(self, clusters, centroids):
      result = 0
      for i in range(0, len(centroids)):
        for j in clusters[i]:
          result += (self.EuclideanDistance(centroids[i],j))
      return result



  def ObjetiveFunction(self, clusters, centroids):
    """
    This function calculates the objective function value for a given set of clusters by adding the
    P_Median value and penalty factor, in this case 4, and multiplied by the number of elements in the cluster.
    @param clusters - The "clusters" parameter is a list of lists, where each inner list represents a
    cluster of data points. The objective function is being calculated for these clusters.
    @returns a value that is the sum of the result of the P_Median function applied to the clusters
    parameter and 4 times the length of the clusters parameter.
    """
    value = self.P_Median(clusters, centroids) + 4 * len(clusters)
    return value



  def Solve(self):
    '''
    The function generates random centroids, then it calculates the distance between each point and
    each centroid, and then it assigns each point to the closest centroid. Then it calculates the new
    centroids and it repeats the process until the clusters don't change
    @returns The SSE and the time it took to run the algorithm.
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
        
    sse = self.ObjetiveFunction(newClusters, centroids)
   
    endTime = time.perf_counter()
    # Show the points on the graph.
    # self.ShowPlot(cluster, centroids)
    centroids = [list(np.round(i, 2)) for i in centroids]

    return centroids, sse, (endTime - startTime)



def test():
  try:
    problem = Problem(os.path.join(".", "problems", "prob1.txt"))
    a = Greedy(problem, 4)
    a.Solve()


  except Exception as e:
    print(str(e))


if __name__ == "__main__":
  test()


