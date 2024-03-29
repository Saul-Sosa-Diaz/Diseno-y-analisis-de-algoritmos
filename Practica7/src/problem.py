"""
File: problem.py
Author: Saúl Sosa Díaz
Date: 25/03/2023
Description: This is a Python file that defines a class named "Problem". 
The purpose of this class is to read or generate a matrix of data that represents a problem instance.
"""

from colors import bcolors
import os
import numpy as np


class Problem:
  '''
  It reads a file and stores the data in a matrix
  '''
  def __init__(self, path = None) -> None:
    if path == None:
      self.Generate()
    else:
      self.ReadFile(path)


  def Generate(self):
    '''
    It generates a random matrix of size (rows, columns) with elements rounded to 2 decimals.
    '''
    print(bcolors.OKBLUE +
          'Generating random instance of the problem...' + bcolors.ENDC)
    rows = np.random.randint(low=5, high=30)
    columns = np.random.randint(low=2, high=10)
    coordenateOfPoints = np.round(np.random.uniform(
        low=0.0, high=10.0, size=(rows, columns)), decimals=2)
    print(coordenateOfPoints)
    self.__points = coordenateOfPoints
    self.__numOfPoints = rows
    self.__sizeOfPoints = columns



  def ReadFile(self, file):
    '''
    It reads a file and stores the data in a matrix
    @param file - The file to be read
    '''

    with open(file, "r") as fileContent:
        numPoints = int(fileContent.readline())
        if numPoints < 0:
          raise Exception(
              bcolors.FAIL + "Error in File: " + os.path.basename(file) + " -> The number of Points cannot be negative." + bcolors.ENDC)

        dimensionOfPoints = int(fileContent.readline())
        if dimensionOfPoints < 1:
          raise Exception(
              bcolors.FAIL + "Error in File: " + os.path.basename(file) + " -> The number dimensionOfPoints cannot be less than one." + bcolors.ENDC)

        matrix = np.zeros((numPoints, dimensionOfPoints))

        for i in range(0, numPoints):
          # Returns the vector with the elements of the vector converted to numbers, you have to change the , by .
          coordenates = [
              float(x) for x in fileContent.readline().replace(",", ".").split()]
          matrix[i] = coordenates

        self.__points = matrix
        self.__numOfPoints = numPoints
        self.__sizeOfPoints = dimensionOfPoints


  def GetPoints(self):
    return self.__points

  def GetNumOfPoints(self):
    return self.__numOfPoints

  def GetSizeOfPoints(self):
    return self.__sizeOfPoints



def test():
  try:
    a = Problem()
    b = Problem(r"E:\Cosas\universidad\tercero\Diseno-y-analisis-de-algoritmos\Practica7\problems\prob1.txt")
    
    print(a.GetNumOfPoints())
    print(a.GetSizeOfPoints())

    print(b.GetPoints())
    print(b.GetNumOfPoints())
    print(b.GetSizeOfPoints())

  except Exception as e:
    print(str(e))


if __name__ == "__main__":
  test()
