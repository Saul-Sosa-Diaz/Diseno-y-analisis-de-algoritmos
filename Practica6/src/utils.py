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
    problems = []
    names = []
    for i in range(0,10):
        matrix= np.random.randint(50, size=(4, 4))
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
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', type=float, help='Limit Run time in seconds')
    parser.add_argument('-g', action='store_true',
                        help='Generate random instance of the problem')
    parser.add_argument(
        '-d', type=str, help='Path to the directory with the problems')
    args = parser.parse_args()
    greedy = Greedy()
    bf = BruteForce()
    dp = DP()
    if args.t:
        greedy.Set_exceeded(args.t)
        bf.Set_exceeded(args.t)
        dp.Set_exceeded(args.t)

    problems = []
    names = []
    if args.g:
        print('Generating random instance of the problem...')
        problems,names = generator()
        
    else:
        if not args.d:
            print('You need a path to the directory')
            exit()
        elif not os.path.isdir(args.d):
            print('The path provided is not a valid directory')
            exit()
        else:
            directory_path = args.d
            problems, names = readFiles(directory_path)
    table = []
    
    for i, problem in enumerate(problems):
        row = [names[i]]
        row.append(bf.Solve(problem)) # Brute force value
        timebf = bcolors.WARNING + "Excessive" + \
            bcolors.ENDC if bf.Get_time() > 60 else bf.Get_time()*1000 # Brute force time in ms
        row.append(timebf)
        row.append(bf.Get_path())

        #Dynamic programming
        row.append(dp.Solve(problem))  # Dynamic programming value
        timedp = bcolors.WARNING + "Excessive" + \
            bcolors.ENDC if dp.Get_time() > 60 else dp.Get_time() * 1000  # Dynamic programming force time in ms
        row.append(timedp)
        row.append(dp.Get_path())

        #Greedy
        row.append(greedy.Solve(problem))  # Greedy force value
        timegreedy = bcolors.WARNING + "Excessive" + \
            bcolors.ENDC if greedy.Get_time() > 60 else greedy.Get_time() * 1000  # Greedy force time in ms
        row.append(timegreedy)
        row.append(greedy.Get_path())
        table.append(row)
    
    print(tabulate.tabulate(table, headers=[
        "Name", "Brute force Value", "Brute force time (ms)", "Brute force path", "Dynamic programming Value", "Dynamic programming time (ms)", "Dynamic programming path", "greedy Value", "greedy time (ms)", "greedy path"], tablefmt="github", stralign="center"))

if "__main__" == __name__:
  menu()
