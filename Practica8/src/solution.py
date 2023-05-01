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

  def PrintSolutionGreedy(self, nameOfProblem, n, k, m, z, S ,CPU):
    table = [[nameOfProblem, n, k, m, z, S, CPU]]
    print(tabulate.tabulate(table, headers=[
        "Problem", "n","K", "m", "z", "S", "CPU"], tablefmt="github", stralign="center"))

  def PrintSolutionGrasp(self, nameOfProblem, n, k, m, i, lrc, z, S, CPU):
    table = [[nameOfProblem, n, k, m, i, lrc, z, S, CPU]]
    print(tabulate.tabulate(table, headers=[
        "Problem", "n", "K", "m", "iteration","|lrc|","z", "S", "CPU"], tablefmt="github", stralign="center"))
    
  def PrintSolutionGreedyInFile(self, nameOutFile, nameOfProblem, n, k, m, z, S, CPU):
    table = None
    table = [[nameOfProblem, n, k, m, z, S, CPU]]
    nameOutFile += "_Greedy.csv"
    with open(nameOutFile, mode='a', newline='') as csvFile:
      writer = csv.writer(csvFile)
      headers = [
          "Problem", "n", "K", "m", "z", "S", "CPU"]
      # If the file is empty, write the headers
      if csvFile.tell() == 0:
        writer.writerow(headers)

      writer.writerow(table[0])

  def PrintSolutionGraspInFile(self, nameOutFile, nameOfProblem, n, k, m, i, lrc, z, S, CPU):
      table = None
      table = [[nameOfProblem, n, k, m, i, lrc, z, S, CPU]]
      nameOutFile += "_Grasp.csv"
      with open(nameOutFile, mode='a', newline='') as csvFile:
        writer = csv.writer(csvFile)
        headers = [
            "Problem", "n", "K", "m", "iteration", "|lrc|", "z", "S", "CPU"]
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
