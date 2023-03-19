from TSP import TSP
import numpy as np
import itertools
import time


class BruteForce(TSP):
  def __init__(self, exceeded=60) -> None:
    self.__value = 0
    self.__time = 0
    self.__path = None
    self.__exceeded = exceeded

  def Solve(self, matrix):
    value = 0
    start_time = time.perf_counter()
    # Get the number of destinations in the distance matrix
    num_destinations = len(matrix)
    # Create a list of all destination indices
    destinations = list(range(num_destinations))
    
    # Initialize the best distance and best path variables to infinity and None, respectively
    best_distance = float('inf')
    best_path = None
    # Generate all possible permutations of destinations
    for path in itertools.permutations(destinations):
      actual_time = time.perf_counter()
      if (actual_time - start_time) > self.__exceeded:
        end_time = time.perf_counter()
        self.__path = best_path
        self.__time = end_time - start_time
        value = best_distance
        self.__value = value
        return value
      # Calculate the total distance traveled for this path
      total_distance = 0
      for i in range(num_destinations - 1):
        total_distance += matrix[path[i]][path[i+1]]
      # add the distance from the last destination to the first
      total_distance += matrix[path[-1]][path[0]]

      # Update the best distance and best path if this path has a shorter distance
      if total_distance < best_distance:
        best_distance = total_distance
        best_path = path
    
    end_time = time.perf_counter()
    self.__time = end_time - start_time
    self.__path = best_path
    value = best_distance
    self.__value = value
    return value


def main():
  try:
    a = BruteForce()
    v = np.array([[0., 25., 10., 15.],
                  [25., 0., 10., 45.],
                  [10., 10., 0., 5.],
                  [15., 45., 5., 0.]])
    print(a.Solve(v))

  except Exception as e:
    print(str(e))


if __name__ == "__main__":
  main()
