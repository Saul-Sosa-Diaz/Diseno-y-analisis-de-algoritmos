"""
File: algorith.py
Author: Saúl Sosa Díaz
Date: 25/03/2023
Description: Implementation of some algorithms commonly used in data science, including the calculation of 
Euclidean distance between two points in a vector space and the calculation of centroids for clusters of points.
"""

from colors import bcolors
from install import install
import numpy as np
import math
import time

try:
    import typeguard
except ImportError:
    install('typeguard')
    import typeguard


class Algorithm:
    ''' 
      This class implements some algorithms commonly used in data science.
    '''
    def __init__(self) -> None:
        pass

    
    def EuclideanDistance(self, p1 : list, p2 : list):
      '''
        This function calculates the Euclidean distance between two points in a vector space.
        Args:
            p1 (list): List representing the first point.
            p2 (list): List representing the second point.
        Returns:
            float: The Euclidean distance between the two points.
        Raises:
            Exception: If the two points do not have the same number of dimensions.
      '''
      # Verify that the points belong to the same vector space
      if len(p1) != len(p2):
         raise Exception(bcolors.FAIL + 
                         "Error in EuclideanDistance -> The points must have the same dimensions." + bcolors.ENDC + 
                         "\nLength of p1: " + str(len(p1)) + "\nLength of p2: " + str(len(p2)))
     
      acc = 0
      for i in range(0, len(p1)):
        acc += (p1[i]-p2[i])**2
      acc = math.sqrt(acc)
      return acc
    


    def CalculateCentroids(self, cluster: list):
      '''This function calculates the centroid of a given cluster of points.
      
      Parameters
      ----------
      cluster : list
        The parameter "cluster" is a list of points that belong to a particular cluster. Each point is
      represented as a list of numerical values, where each value corresponds to a feature or attribute of
      the point. The function calculates the centroid of the cluster, which is the average of all the
      points in the
      
      Returns
      -------
        the centroid of the given cluster, which is calculated by taking the mean of all the points in the
      cluster.
      
      '''
      if (len(cluster) == 0):
         return
      centroid = np.zeros(len(cluster[0]))
      for point in cluster:
        centroid += point
      centroid /= len(cluster)
      return centroid
    

    def SSE(self, clusters, centroids):
      '''The function calculates the sum of squared errors (SSE) between the centroids and the data points in
      each cluster.

      Parameters
      ----------
      clusters
        A list of lists where each inner list contains the data points assigned to a particular cluster.
      centroids
        A list of centroid points for each cluster in the clustering algorithm.

      Returns
      -------
        the sum of squared errors (SSE) for a given set of clusters and their centroids.

      '''
      result = 0
      for i in range(0, len(centroids)):
        for j in clusters[i]:
          result += (self.EuclideanDistance(centroids[i],j))**2
      return result
    



    def P_Median(self, clusters):
      '''The function calculates the sum of Euclidean distances between the centroid and all other points in
      each cluster and returns the total sum.
      
      Parameters
      ----------
      clusters
        A list of clusters, where each cluster is represented as a list of points. The first point in each
      cluster is the centroid of that cluster, and the remaining points are the data points assigned to
      that cluster. The function calculates the P-Median objective function value for the given clusters.
      
      Returns
      -------
        The function `P_Median` is returning the sum of the Euclidean distances between the centroid of
      each cluster and all the other points in the same cluster.
      
      '''
      result = 0
      for cluster in clusters:
        for point in cluster[1:]:
          result += self.EuclideanDistance(cluster[0], point)
      
      return result

    

def test():
  try:
    a = Algorithm()
    p1 = [7.8, 0.1, 6.6]
    p2 = [9.2, 1.2, 9.7]
    print(a.EuclideanDistance(p1,p2))
  

  except Exception as e:
    print(str(e))


if __name__ == "__main__":
  test()
