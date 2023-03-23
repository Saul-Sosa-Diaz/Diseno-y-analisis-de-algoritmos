import os
import glob
from install import install
from colors import bcolors

try:
    import numpy as np
except ImportError:
    install('numpy')
    import numpy as np

def readFile(file):
    '''
    Reads a text file and constructs its corresponding distance matrix.
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
        
        matrix = np.zeros((numPoints,dimensionOfPoints))

        for i in range(0, numPoints):
           # Devuelve el vector los elementos del vector coonvertidos a numeros, hay que cambiar las , por .
           coordenates = [float(x) for x in fileContent.readline().replace(",", ".").split()]
           matrix[i] = coordenates

        return matrix


if "__main__" == __name__:
  print(readFile(r"E:\Cosas\universidad\tercero\Diseno-y-analisis-de-algoritmos\Practica7\problems\prob1.txt"))
