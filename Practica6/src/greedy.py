from TSP import TSP
import numpy as np
import time

class greedy(TSP):
  def __init__(self) -> None:
    self.__value = 0
    self.__time = 0
    self.__visited = [False] * 4
    self.__path = None
  
  def solve(self, matrix):
    value = 0
    start_time = time.perf_counter()
    actualNode = 0
    self.__visited[0] = True
    path = [0]
    while (not all(self.__visited)):
      actual_time = time.perf_counter()

      # Si se pasa del minuto
      if (actual_time - start_time) > 60:
        end_time = time.perf_counter()
        self.__time = end_time - start_time
        self.__value = value
        return value
      
      i = 0
      min = float('inf')
      index_smallest_element = 0
      while i < len(matrix[actualNode]):
        if matrix[actualNode,i] < min and self.__visited[i] == False:
          min = matrix[actualNode,i]
          index_smallest_element = i
        i += 1

      value += min
      actualNode = index_smallest_element
      self.__visited[actualNode] = True
      path.append(actualNode)
    
    end_time = time.perf_counter()
    self.__time = end_time - start_time
    self.__path = path
    value += matrix[actualNode,0] # Volver al original
    self.__value = value

    return value
      

def main():
  try:
    a = greedy()
    v = np.array([[0., 25., 10., 15.], 
                  [25., 0., 10., 45.],
                  [10., 10., 0., 5.], 
                  [15., 45., 5., 0.]])
    print(a.solve(v))

  except Exception as e:
    print(str(e))


if __name__ == "__main__":
  main()
