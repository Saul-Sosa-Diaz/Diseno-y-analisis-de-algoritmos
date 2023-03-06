import random
import time
from install_function import install
from mergeSort import MergeSort
from quickSort import QuickSort

try:
    import tabulate
except ImportError:
    install('tabulate')
    import tabulate

def menu() -> None:
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
        randomlist = random.sample(range(-10000, 10000), n)

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
    print("The average of Merge Sort is: ", sum(result_merge) / len(result_merge))
    print("The average of Quick Sort is: ", sum(result_quicksort) / len(result_quicksort))



if "__main__" == __name__:
  menu()
