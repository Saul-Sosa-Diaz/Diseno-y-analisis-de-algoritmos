"""
File: solution.py
Author: Saúl Sosa Díaz
Date: 25/03/2023
Description: This code defines a class named "Solution" that manages solutions to problems. 
It includes two methods, "PrintSolution" and "PrintSolutionInFile", both of which print out the results of an algorithm run on a dataset.
"""


import csv
from install import install 
try:
    import tabulate
except ImportError:
    install('tabulate')
    import tabulate


class Solution:

  def __init__(self) -> None:
    '''
    Manages solutions to problems
    '''
    pass

  def PrintSolution(self, nameOfFile, clusters ,numberOfPoints, SSE, CPU, numberOfClusters=3, cardinality=None):
    '''
    It prints a table with the results of the algorithm
    @param nameOfFile - The name of the file that contains the data points.
    @param numberOfPoints - number of points in the dataset
    @param SSE - Sum of Squared Errors
    @param CPU - The time it took to run the algorithm
    @param [numberOfClusters=3] - number of clusters
    @param cardinality - the number of points in the LRC
    '''
    table = None
    if cardinality == None: # Print kmeans
      table = [[nameOfFile, 
                clusters, 
              numberOfPoints,
              numberOfClusters,
              SSE,
              CPU]
              ]
      print(tabulate.tabulate(table, headers=[
          "Problem", "Centroids","m", "k", "Objetive Value", "CPU"], tablefmt="github", stralign="center"))
    else: # Print GRASP
      table = [[nameOfFile,
                clusters,
               numberOfPoints,
               numberOfClusters,
               cardinality,
               SSE,
               CPU]
               ]
      print(tabulate.tabulate(table, headers=[
          "Problem", "Point of services", "m", "k", "|LRC|", "Objetive Value", "CPU"], tablefmt="github", stralign="center"))
    

  def PrintSolutionGVNS(self, nameOfFile, clusters, numberOfPoints, SSE, CPU, kInicial, kFinal ):
      table = None
      table = [[nameOfFile,
                  clusters,
                  numberOfPoints,
                  kInicial,
                  kFinal,
                  SSE,
                  CPU]
                ]
      print(tabulate.tabulate(table, headers=[
            "Problem", "Points of services", "m", "k initial", "k final","Objetive Value", "CPU"], tablefmt="github", stralign="center"))


  def PrintSolutionGVNSInFile(self, nameOutFile, nameOfFile, clusters, numberOfPoints, SSE, CPU, kInicial, kFinal):
      table = None
      table = [[nameOfFile,
                clusters,
                numberOfPoints,
                kInicial,
                kFinal,
                SSE,
                CPU]
               ]
      nameOutFile += "_GVNS.csv"
      with open(nameOutFile, mode='a', newline='') as csvFile:
        writer = csv.writer(csvFile)
        headers = [
            "Problem", "Points of services", "m", "k initial", "k final", "Objetive Value", "CPU"]
        # If the file is empty, write the headers
        if csvFile.tell() == 0:
          writer.writerow(headers)

        writer.writerow(table[0])




  def PrintSolutionInFile(self, nameOutFile, clusters ,nameInFile, numberOfPoints, SSE, CPU, numberOfClusters=3, cardinality=None):
    '''
    It takes in a bunch of parameters, and writes them to a CSV file. 
    
    The CSV file is created if it doesn't exist, and if it does exist, it appends the new data to the
    end of the file. 
    The data is written to the CSV file in a single row. 
    @param nameOutFile - the name of the file to write to
    @param nameInFile - the name of the file that contains the data points
    @param numberOfPoints - number of points in the dataset
    @param SSE - Sum of Squared Errors
    @param CPU - The time it took to run the algorithm
    @param [numberOfClusters=3] - The number of clusters to be used in the k-means algorithm.
    @param cardinality - the number of points in the LRC
    '''
    table = None

    if cardinality == None:  # Print kmeans
      table = [[nameInFile,
                clusters,
                numberOfPoints,
                numberOfClusters,
                SSE,
                CPU]
               ]
      nameOutFile += "_kmeans.csv"

      with open(nameOutFile, mode='a', newline='') as csvFile:
        writer = csv.writer(csvFile)
        headers = [
            "Problem", "Centroids", "m", "k", "Objetive Value", "CPU"]
        # If the file is empty, write the headers
        if csvFile.tell() == 0:
          writer.writerow(headers)
        
        writer.writerow(table[0])

    else:  # Print GRASP
      table = [[nameInFile,
                clusters,
               numberOfPoints,
               numberOfClusters,
               cardinality,
               SSE,
               CPU]
               ]
      nameOutFile += "_GRASP.csv"

      with open(nameOutFile, mode='a', newline='') as csvFile:
        writer = csv.writer(csvFile)
        headers = [
            "Problem", "Point of services", "m", "k", "|LRC|", "Objetive Value", "CPU"]
        # If the file is empty, write the headers
        if csvFile.tell() == 0:
          writer.writerow(headers)

        writer.writerow(table[0])




def test():
  try:
    a = Solution()
    a.PrintSolution("test.test",15,10.0,0.000015,4)
    print()
    a.PrintSolution("test.test", 15, 10.0, 0.000015, 4, 4)
    a.PrintSolutionInFile("test_solution", "test.test", 15, 10.0, 0.000015, 4)
    a.PrintSolutionInFile("test_solution", "test.test",
                          15, 10.0, 0.000015, 4, 4)
  except Exception as e:
    print(str(e))


if __name__ == "__main__":
  test()
