import argparse
from problem import *
from colors import bcolors




def menu() -> None:
    '''
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

    # Indicate the path to the file with the problem
    if not args.f:
        problem = Problem()
    elif not os.path.isfile(args.f):
        print(bcolors.FAIL + 'The path provided is not a valid file' + bcolors.ENDC)
        exit()
    else:
        file_path = args.f
        problem = Problem(file_path)

    
    




if "__main__" == __name__:
  menu()
