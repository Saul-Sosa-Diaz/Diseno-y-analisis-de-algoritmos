import os
import glob
from install import install
from colors import bcolors
import re

try:
    import numpy as np
except ImportError:
    install('numpy')
    import numpy as np

def readFile(file):
    with open(file, "r") as fileContent:
        numNodes = int(fileContent.readline())
        if numNodes < 0:
          raise Exception(
              bcolors.FAIL + "Error in File: " + os.path.basename(file) + " -> The number of nodes in a network cannot be negative." + bcolors.ENDC)
        matrix = np.zeros((numNodes,numNodes))
        currentNode = 1
        while (currentNode <= numNodes):
            i = 0
            while i < numNodes - currentNode: # Evitar las líneas vacías
                line = fileContent.readline().strip()
                while not line:
                    line = fileContent.readline().strip()
                value = int(line.split()[-1]) #Coger el último elemento
                matrix[currentNode - 1, i + currentNode] = value
                i += 1
            currentNode += 1
        # Completar la matriz en la diagonal inferior
        for i in range(0, numNodes):
            j = 0
            while j < i:
                matrix[i,j] = matrix[j,i]
                j += 1
        return matrix


def readFiles(path):
    problems = []
    result_files = []
    files = glob.glob(os.path.join(path, "*"))
    for file in files:
        try:
          problems.append(readFile(file))
          result_files.append(os.path.basename(file))
        except Exception as e:
          print(str(e) + " This file will not be considered.")
          continue
    return problems, result_files

if "__main__" == __name__:
  readFiles(r"E:\Cosas\universidad\tercero\Diseno-y-analisis-de-algoritmos\Practica6\problems")
