import argparse
import os

from colors import bcolors
from readfile import *



def menu() -> None:
    '''
    Manages and displays the results of problems solved with dynamic programming, brute force and greedy.
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', type=str, help='Path to the file with the points')
    args = parser.parse_args()
    coordenateOfPoints = None
    # Indicate the path to the file with the problem
    if not args.d:
        print(bcolors.OKBLUE + 'Generating random instance of the problem...' + bcolors.ENDC)
        
        rows = np.random.randint(low=2, high=15)
        columns = np.random.randint(low=3, high=10)

        coordenateOfPoints = np.round(np.random.uniform(
            low=0.0, high=10.0, size=(rows, columns)), decimals=2)  # Generar una matriz aleatoria de 10x5 con elementos redondeados a 2 decimales
        
        print(coordenateOfPoints)
    elif not os.path.isfile(args.d):
        print(bcolors.FAIL + 'The path provided is not a valid file' + bcolors.ENDC)
        exit()
    else:
        directory_path = args.d
        coordenateOfPoints = readFile(directory_path)
    
    
    




if "__main__" == __name__:
  menu()
