import os
import glob
from install import install

try:
    import numpy as np
except ImportError:
    install('numpy')
    import numpy as np

def readFile(file):
    with open(file, "r") as fileContent:
        numNodes = int(fileContent.readline())
        matrix = np.zeros((numNodes,numNodes))
        currentNode = 1
        
        while (currentNode <= numNodes):
            i = 0
            while i < numNodes - currentNode: 
                value = int(fileContent.readline().split()[-1]) #Coger el último elemento
                print(value)
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
    files = glob.glob(os.path.join(path, "*"))
    for file in files:
        problems.append(readFile(file))


if "__main__" == __name__:
  readFiles(r"E:\Cosas\universidad\tercero\Diseno-y-analisis-de-algoritmos\Practica6\problems")
