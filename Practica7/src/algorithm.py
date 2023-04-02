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
      '''
        This function calculates the centroid of a cluster of points.
        Args:
            cluster (list): A list of points in the same cluster.
        Returns:
            numpy.ndarray: A numpy array representing the centroid of the cluster.
      '''
      if (len(cluster) == 0):
         return
      centroid = np.zeros(len(cluster[0]))
      for point in cluster:
        centroid += point
      centroid /= len(cluster)
      return centroid
    
    def SSE(self, clusters, centroids):
      result = 0
      for i in range(0, len(centroids)):
        for j in clusters[i]:
          result += (self.EuclideanDistance(centroids[i],j))**2
      return result
    
    def P_Median(self, clusters):
      result = 0
      for cluster in clusters:
        servicePoint = cluster[0]
        for point in cluster[1:]:
          result += self.EuclideanDistance(servicePoint, point)
      
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
