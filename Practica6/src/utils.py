import random
import time
import argparse
from install import install
from colors import bcolors

try:
    import tabulate
except ImportError:
    install('tabulate')
    import tabulate





def debug_mode() -> None:
    '''
    It enters debug mode, prompts the user for a positive problem size, 
    and the algorithm to use, and displays the unsolved and solved problem.
    '''

    pass




def normal_mode() -> None:
    '''
    Benchmarks the performance of Merge Sort and Quick Sort algorithms 
    by generating random lists of integers and measuring the time taken by each algorithm to sort them.
    '''
    pass

def menu() -> None:
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", '--debug', action='store_true',
                    help='Enables debug mode')
    args = parser.parse_args()
    
    if args.debug :
        debug_mode()
    else:
        normal_mode()



if "__main__" == __name__:
  menu()
