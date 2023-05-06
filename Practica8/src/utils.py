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
from math import ceil
from solution import Solution
from colors import bcolors
from branchAndBound import BranchAndBound


def menu() -> None:
    '''
    Manages program parameters, creates problems, solves them and displays the solution.
    '''

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', type=str, help='Path to the file with the points')
    parser.add_argument('-o', type=str, help='Name of the output file where the solution will be dumped')
    parser.add_argument('-m', type=int, help='Modify the number of points of the solution.')
    parser.add_argument('-c', type=int, help='Modify the cardinality of the grasp LCR')
    parser.add_argument('-i', type=int, help='Iterations of grasp 10 by default')
    
    args = parser.parse_args()
    problem = None
    nameOfProblem = ""
    greedy = None
    grasp = None
    m = 3
    c = 3
    i = 10
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
        
    # Number of points by default.
    if not args.m and args.m != 0:
        greedy = GRASP(problem, m, 1)
        # Cardinality not indicated
        if not args.c and args.c != 0:
            grasp = GRASP(problem, m)
        else: 
            c = int(args.c)
            if c < 0:
                raise Exception(
                    bcolors.FAIL + "Error in c argument cannot be negative or 0." + bcolors.ENDC)
            grasp = GRASP(problem, cardinality=c)
    else:
        m = int(args.m)
        if m <= 2:
            raise Exception(
                bcolors.FAIL + "Error in m argument cannot be less than 2." + bcolors.ENDC)
        greedy = GRASP(problem, m, 1)
        # Cardinality not indicated
        if not args.c and args.c != 0:
            grasp = GRASP(problem, m)
        else:
            c = int(args.c)
            if c < 0:
                raise Exception(
                    bcolors.FAIL + "Error in c argument cannot be negative." + bcolors.ENDC)
            grasp = GRASP(problem, m, c)

    if args.i:
        i = int(args.i)

    #Resolve the algorithms    
    solutionGreedy, objetiveValueGreedy, CPUGreedy = greedy.Grasp(1)
    solutionGrasp, objetiveValueGrasp, CPUGrasp = grasp.Grasp(i)
    bab = BranchAndBound(objetiveValueGrasp, problem, m)
    solutionBab, objetiveValueBab, generatedNodes, CPUBab = bab.BranchAndBound()
    
    #Print results
    if not args.o:
        print(bcolors.UNDERLINE + "Greedy" + bcolors.ENDC)
        solution.PrintSolutionGreedy(nameOfProblem, 
                                     problem.GetNumOfPoints(), 
                                     problem.GetSizeOfPoints(), 
                                     m, 
                                     round(objetiveValueGreedy,2), 
                                     solutionGreedy,
                                     CPUGreedy)
        
        print()
        print(bcolors.UNDERLINE + "GRASP" + bcolors.ENDC)
        solution.PrintSolutionGrasp(nameOfProblem,
                                     problem.GetNumOfPoints(),
                                     problem.GetSizeOfPoints(),
                                     m,
                                     i,
                                     c,
                                     round(objetiveValueGrasp, 2),
                                     solutionGrasp,
                                     CPUGrasp)
        print()
        print(bcolors.UNDERLINE + "Branch and Bound" + bcolors.ENDC)
        solution.PrintSolutionBaB(nameOfProblem,
                                    problem.GetNumOfPoints(),
                                    problem.GetSizeOfPoints(),
                                    m,
                                    round(objetiveValueBab, 2),
                                    solutionBab,
                                    CPUBab,
                                    generatedNodes)

    else:
        solution.PrintSolutionGreedyInFile(args.o,
                                           nameOfProblem,
                                           problem.GetNumOfPoints(),
                                           problem.GetSizeOfPoints(),
                                           m,
                                           round(objetiveValueGreedy,2),
                                           solutionGreedy,
                                           CPUGreedy)
        print(bcolors.OKGREEN + "Created greedy file" + bcolors.ENDC)
       
        solution.PrintSolutionGraspInFile(args.o, 
                                          nameOfProblem,
                                           problem.GetNumOfPoints(),
                                           problem.GetSizeOfPoints(),
                                           m,
                                           i,
                                           c,
                                           round(objetiveValueGrasp, 2),
                                           solutionGrasp,
                                           CPUGrasp)
        print(bcolors.OKGREEN + "Created GRASP file" + bcolors.ENDC)

        solution.PrintSolutionBaBInFile(args.o,
                                        nameOfProblem,
                                        problem.GetNumOfPoints(),
                                        problem.GetSizeOfPoints(),
                                        m,
                                        round(objetiveValueBab, 2),
                                        solutionBab,
                                        CPUBab,
                                        generatedNodes)



if "__main__" == __name__:
  menu()
