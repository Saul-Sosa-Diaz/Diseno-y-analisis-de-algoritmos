"""
File: utils.py
Author: Saúl Sosa Díaz
Date: 25/03/2023
Description: The code is a Python script that implements a menu to solve clustering problems using two algorithms: Greedy and GRASP. 
The menu takes as input a file with the points of the problem and allows to specify the number of clusters and the cardinality for the GRASP algorithm. 
The solution of the problem is displayed on the screen or written to an output file.
"""

import argparse
from problem import *
from grasp import GRASP
from greedy import Greedy
from math import ceil
from solution import Solution
from colors import bcolors


def menu() -> None:
    '''
    Manages program parameters, creates problems, solves them and displays the solution.
    '''

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', type=str, help='Path to the file with the points')
    parser.add_argument(
        '-o', type=str, help='Name of the output file where the solution will be dumped')
    parser.add_argument(
        '-k', type=int, help='Modify the number of clusters of the default algorithms.')
    parser.add_argument(
        '-c', type=int, help='Modify the cardinality of the grasp CLR')
    args = parser.parse_args()
    problem = None
    nameOfProblem = ""
    greedy = None
    grasp = None
    k = 2
    c = 3
    solution = Solution()

    # Indicate the path to the file with the problem
    if not args.f:
        problem = Problem()
        nameOfProblem = "Random instance"
    elif not os.path.isfile(args.f):
        print(bcolors.FAIL + 'The path provided is not a valid file' + bcolors.ENDC)
        exit()
    else:
        file_path = args.f
        problem = Problem(file_path)
        nameOfProblem = os.path.basename(file_path)
    k = ceil(problem.GetNumOfPoints() * 0.1) 
    
    if k < 2:
        k = 2
        
    # Number of clusters by default.
    if not args.k and args.k != 0:
        greedy = Greedy(problem, k)
        # Cardinality not indicated
        if not args.c and args.c != 0:
            grasp = GRASP(problem, k)
        else: 
            c = int(args.c)
            if c < 0:
                raise Exception(
                    bcolors.FAIL + "Error in c argument cannot be negative or 0." + bcolors.ENDC)
            grasp = GRASP(problem, cardinality=c)
    else:
        k = int(args.k)
        if k <= 2:
            raise Exception(
                bcolors.FAIL + "Error in K argument cannot be less than 2." + bcolors.ENDC)
        greedy = Greedy(problem, k)
        # Cardinality not indicated
        if not args.c and args.c != 0:
            grasp = GRASP(problem, k)
        else:
            c = int(args.c)
            if c < 0:
                raise Exception(
                    bcolors.FAIL + "Error in c argument cannot be negative." + bcolors.ENDC)
            grasp = GRASP(problem, k, c)

    #Resolve the algorithms    
    centroids,SSEGreedy, timeGreedy = greedy.Solve()
    pointOfservices,SSEGrasp, timeGrasp = grasp.Grasp()
    
    if not args.o:
        print()
        # Gready
        solution.PrintSolution(
            nameOfProblem, centroids, problem.GetNumOfPoints(), SSEGreedy, timeGreedy, k)
        print()
        # Grasp
        solution.PrintSolution(
            nameOfProblem, pointOfservices, problem.GetNumOfPoints(), SSEGrasp, timeGrasp, k, c)
        print()
    else:
        # Gready
        solution.PrintSolutionInFile(
            args.o, centroids, nameOfProblem,  problem.GetNumOfPoints(), SSEGreedy, timeGreedy, k)
        #GRASP
        solution.PrintSolutionInFile(
            args.o, pointOfservices, nameOfProblem,  problem.GetNumOfPoints(), SSEGrasp, timeGrasp, k, c)


if "__main__" == __name__:
  menu()
