import random
import time
import argparse
import os
from greedy import Greedy
from bruteForce import BruteForce
from install import install
from colors import bcolors
from readfile import *

try:
    import tabulate
except ImportError:
    install('tabulate')
    import tabulate


def generator():
    problems = []
    names = []
    for i in range(0,10):
        matrix= np.triu(np.random.randint(50, size=(4, 4)))
        for k in range(0, 4):
            j = 0
            while j <= k:
                if k == j:
                    matrix[k, j] = 0
                else: 
                    matrix[k, j] = matrix[j, k]
                j += 1
        problems.append(matrix)
        names.append(f"Random Matrix number: {i}")
        

def menu() -> None:  
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', type=int, help='Limit Run time in seconds')
    parser.add_argument('-g', action='store_true',
                        help='Generate random instance of the problem')
    parser.add_argument(
        '-d', type=str, help='Path to the directory with the problems')
    args = parser.parse_args()
    greedy = Greedy()
    bf = BruteForce()
    if args.t:
        greedy.Set_exceeded(args.t)
        bf.Set_exceeded(args.t)

    problem = []
    names = []
    if args.g:
        print('Generating random instance of the problem...')
        problem,names = generator()
    else:
        if not args.d:
            print('You need a path to the directory')
            exit()
        elif not os.path.isdir(args.d):
            print('The path provided is not a valid directory')
            exit()
        else:
            directory_path = args.d
            problem, names = readFiles(directory_path)



if "__main__" == __name__:
  menu()
