import csv
import os
from install import install 
try:
    import tabulate
except ImportError:
    install('tabulate')
    import tabulate


class Solution:

  def __init__(self) -> None:
    pass

  def PrintSolution(self, nameOfFile, numberOfPoints, SSE, CPU, numberOfClusters=3, cardinality=None):
    table = None
    if cardinality == None: # Print kmeans
      table = [[nameOfFile, 
              numberOfPoints,
              numberOfClusters,
              SSE,
              CPU]
              ]
      print(tabulate.tabulate(table, headers=[
          "Problem", "m", "k", "SSE", "CPU"], tablefmt="github", stralign="center"))
    else: # Print GRASP
      table = [[nameOfFile,
               numberOfPoints,
               numberOfClusters,
               cardinality,
               SSE,
               CPU]
               ]
      print(tabulate.tabulate(table, headers=[
          "Problem", "m", "k", "|LRC|" ,"SSE", "CPU"], tablefmt="github", stralign="center"))
    

  def PrintSolutionInFile(self, nameOutFile ,nameInFile, numberOfPoints, SSE, CPU, numberOfClusters=3, cardinality=None):
    table = None

    if cardinality == None:  # Print kmeans
      table = [[nameInFile,
                numberOfPoints,
                numberOfClusters,
                SSE,
                CPU]
               ]
      nameOutFile += "_kmeans.csv"

      with open(nameOutFile, mode='a', newline='') as csvFile:
        writer = csv.writer(csvFile)
        headers = [
            "Problem", "m", "k", "SSE", "CPU"]
        # If the file is empty, write the headers
        if csvFile.tell() == 0:
          writer.writerow(headers)
        
        writer.writerow(table[0])

    else:  # Print GRASP
      table = [[nameInFile,
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
            "Problem", "m", "k", "|LRC|", "SSE", "CPU"]
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
