import random
import time
import argparse
from install_function import install
from mergeSort import MergeSort
from quickSort import QuickSort
from colors import bcolors

try:
    import tabulate
except ImportError:
    install('tabulate')
    import tabulate

algorithms = {
    "mergesort": 0,
    "quicksort": 1
}

def debug_mode() -> None:
    '''
    It enters debug mode, prompts the user for a positive problem size, 
    and the algorithm to use, and displays the unsolved and solved problem.
    '''

    print(bcolors.WARNING + "Debug Mode Enabled" + bcolors.ENDC)
    n = int(input("Enter the size of the problem:\n"))
    if n < 0:
        raise Exception(
            bcolors.FAIL + "The size of the problem can´t be negative" + bcolors.ENDC)
    algorit = None
    algoritm_to_use = None
    while True:
        print("Enter the algorithm to resolve the program(", ', '.join(list(algorithms.keys())), "):")
        algorit = input().lower().replace(" ", "")
        print(algorit)
        if algorit in algorithms:
            break
        print(bcolors.FAIL + "That is not a correct value, the correct values are: " + bcolors.ENDC,
                list(algorithms.keys()), "\n Try again.")

    if algorithms[algorit] == 0:
        algoritm_to_use = MergeSort()
    else:
        algoritm_to_use = QuickSort()
    randomlist = []
    for i in range(0, n):
        randomlist.append(random.randint(-100000,100000))
    print(bcolors.OKCYAN + "The problem is: " + bcolors.ENDC, randomlist)
    start_time = time.perf_counter()
    solution = algoritm_to_use.Solve(randomlist)
    end_time = time.perf_counter()
    print(bcolors.OKCYAN + "The solution is: " + bcolors.ENDC, solution)
    print(bcolors.OKGREEN + "The time it has taken is: ",
          end_time - start_time,  bcolors.ENDC +"\n")

def normal_mode() -> None:
    '''
    Benchmarks the performance of Merge Sort and Quick Sort algorithms 
    by generating random lists of integers and measuring the time taken by each algorithm to sort them.
    '''

    result_merge = []
    result_quicksort = []
    mergeSort = MergeSort()
    quickSort = QuickSort()
    table = []
    for i in range(0, 10):
        n = random.randint(1000, 4000)
        randomlist = []
        for i in range(0, n):
            randomlist.append(random.randint(-100000, 100000))

        start_time1 = time.perf_counter()
        mergeSort.Solve(randomlist)
        end_time1 = time.perf_counter()
        total_time1 = end_time1 - start_time1
        table.append([n, "Merge Sort",  total_time1])
        result_merge.append(total_time1)

        start_time2 = time.perf_counter()
        quickSort.Solve(randomlist)
        end_time2 = time.perf_counter()
        total_time2 = end_time2 - start_time2
        table.append([n, "Quick Sort",  total_time2])
        result_quicksort.append(total_time2)

    print()
    print(tabulate.tabulate(table, headers=[
        "n", "Type", "Time"], tablefmt="github", stralign="center"))

    print()
    print("The average of Merge Sort is: ",
            sum(result_merge) / len(result_merge))
    print("The average of Quick Sort is: ", sum(
        result_quicksort) / len(result_quicksort))

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
