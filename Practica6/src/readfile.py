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
        numNodes = int(fileContent.readline())
        if numNodes < 0:
          raise Exception(
              bcolors.FAIL + "Error in File: " + os.path.basename(file) + " -> The number of nodes in a network cannot be negative." + bcolors.ENDC)
        matrix = np.zeros((numNodes,numNodes))
        currentNode = 1
        while (currentNode <= numNodes):
            i = 0
            while i < numNodes - currentNode: # Avoid blank lines
                line = fileContent.readline().strip()
                while not line:
                    line = fileContent.readline().strip()
                value = int(line.split()[-1]) # Pick last element
                matrix[currentNode - 1, i + currentNode] = value
                i += 1
            currentNode += 1
        # Complete the matrix in the lower triangle
        for i in range(0, numNodes):
            j = 0
            while j < i:
                matrix[i,j] = matrix[j,i]
                j += 1
        return matrix


def readFiles(path):
    '''
    Reads all files in a directory and outputs their respective arrays and names.
    '''
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
