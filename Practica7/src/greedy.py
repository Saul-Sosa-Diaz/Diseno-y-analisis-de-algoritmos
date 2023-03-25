from algorithm import *
import random 
from problem import Problem
import numpy as np

class greedy(Algorithm):

  @typeguard.typechecked
  def __init__(self, problem : Problem) -> None:
    self.__problem = problem
  
  def Solve(self):
    """
    1: Seleccionar K puntos como centroides iniciales
    2: repeat
    3: Construir K clusters asignando cada punto al centroide más cercano
    4: Recalcular los centroides de cada cluster
    5: until(Ningún punto cambie de cluster)"""

    # Generar centroides alatorios
    centroids = random.sample(range(0, self.__problem.GetNumOfPoints()), 3) #Aquí va una k
    aux = []
    for i in centroids:
      aux.append(self.__problem.GetPoints()[i])
    centroids = aux
    cluster = []
    newClusters = [[]for i in range(0, 3)]  # aqui va k
    newCentroids = []
    while True:
      for i in range(3):  # aqui va k
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
    
    for i in range(0, 3): #Aqui va k
      print("Cluster", i, "length:" , len(cluster[i]))


def main():
  try:
    problem = Problem(
        r"E:\Cosas\universidad\tercero\Diseno-y-analisis-de-algoritmos\Practica7\problems\prob1.txt")
    a = greedy(problem)
    a.Solve()


  except Exception as e:
    print(str(e))


if __name__ == "__main__":
  main()


