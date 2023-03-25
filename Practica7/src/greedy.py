from algorithm import *
import random 
from problem import Problem
import numpy as np

class greedy(Algorithm):

  @typeguard.typechecked
  def __init__(self, problem : Problem, k : int = 3) -> None:
    self.__problem = problem
    self.__k = k
  
  def Solve(self):
    """
    1: Seleccionar K puntos como centroides iniciales
    2: repeat
    3: Construir K clusters asignando cada punto al centroide más cercano
    4: Recalcular los centroides de cada cluster
    5: until(Ningún punto cambie de cluster)"""

    # Generar centroides alatorios
    centroids = random.sample(range(0, self.__problem.GetNumOfPoints()), self.__k) 
    aux = []
    for i in centroids:
      aux.append(self.__problem.GetPoints()[i])
    centroids = aux
    cluster = []
    newClusters = [[]for i in range(0, self.__k)]  
    newCentroids = []
    while True:
      for i in range(self.__k):  
        newClusters[i] = []
      for j in range(0, self.__problem.GetNumOfPoints()):
        min = float('inf')
        minIndex = -1
        for i, centroid in enumerate(centroids):
          if min > self.EuclideanDistance(self.__problem.GetPoints()[j], centroid):
            minIndex = i
            min = self.EuclideanDistance(self.__problem.GetPoints()[j], centroid)
        newClusters[minIndex].append(self.__problem.GetPoints()[j])

      for i in newClusters:
        newCentroids.append(self.CalculateCentroids(i))
      
      if newClusters == cluster:
        break
      else:
        cluster = newClusters
        centroids = newCentroids
    
    for i in range(0, self.__k): 
      print("Cluster", i, "length:" , len(cluster[i]))


def main():
  try:
    problem = Problem(
        r"E:\Cosas\universidad\tercero\Diseno-y-analisis-de-algoritmos\Practica7\problems\prob1.txt")
    a = greedy(problem,3)
    a.Solve()


  except Exception as e:
    print(str(e))


if __name__ == "__main__":
  main()


