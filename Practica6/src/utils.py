import argparse
import os
from greedy import Greedy
from bruteForce import BruteForce
from dynamicProgramming import DP
from install import install
from colors import bcolors
from readfile import *

try:
    import tabulate
except ImportError:
    install('tabulate')
    import tabulate


def generator():
    '''
    Generates 10 random instances to solve, returns two lists, 
    the first with the distance matrices of the problems and their names.
    '''
    problems = []
    names = []
    for i in range(0,10):
        matrix= np.random.randint(50, size=(4, 4))

        # Fill in the lower triangle with the same numbers as in the upper triangle.
        for k in range(0, 4):
            j = 0
            while j <= k:
                if k == j:
                    matrix[k, j] = 0
                else: 
                    matrix[k, j] = matrix[j, k]
                j += 1
        problems.append(matrix)
        names.append(f"Instance: {i}") 
    return problems,names




def menu() -> None:
    '''
    Manages and displays the results of problems solved with dynamic programming, brute force and greedy.
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', type=float, help='Limit Run time in seconds')
    parser.add_argument('-d', type=str, help='Path to the directory with the problems')
    args = parser.parse_args()
    greedy = Greedy()
    bf = BruteForce()
    dp = DP()
    problems = []
    names = []

    # Indicate to the algorithm a maximum time
    if args.t: 
        greedy.Set_exceeded(args.t)
        bf.Set_exceeded(args.t)
        dp.Set_exceeded(args.t)
    
    # Indicate the path to the folder with the problems
    if not args.d:
        print('Generating random instance of the problem...')
        problems, names = generator()
    elif not os.path.isdir(args.d):
        print(bcolors.FAIL + 'The path provided is not a valid directory' + bcolors.ENDC)
        exit()
    else:
        directory_path = args.d
        problems, names = readFiles(directory_path)
    table = []
    
    for i, problem in enumerate(problems):
        row = [names[i]]
        # Brute force
        row.append(bf.Solve(problem)) # value
        timeBf = bcolors.WARNING + "Excessive" + \
            bcolors.ENDC if bf.Get_time() > 60 else bf.Get_time()*1000 # Time in ms
        row.append(timeBf)
        row.append(bf.Get_path())
        #Dynamic programming
        
        row.append(dp.Solve(problem))  # Value
        timeDp = bcolors.WARNING + "Excessive" + \
            bcolors.ENDC if dp.Get_time() > 60 else dp.Get_time() * 1000  # Time in ms
        row.append(timeDp)
        row.append(dp.Get_path())
        
        #Greedy
        row.append(greedy.Solve(problem))  # Value
        timeGreedy = bcolors.WARNING + "Excessive" + \
            bcolors.ENDC if greedy.Get_time() > 60 else greedy.Get_time() * 1000  # Time in ms
        row.append(timeGreedy)
        row.append(greedy.Get_path())

        table.append(row)
    
    print(tabulate.tabulate(table, headers=[
        "Name", "Brute force Value", "Brute force time (ms)", "Brute force path", "Dynamic programming Value", "Dynamic programming time (ms)", "Dynamic programming path", "greedy Value", "greedy time (ms)", "greedy path"], tablefmt="github", stralign="center"))




if "__main__" == __name__:
  menu()
