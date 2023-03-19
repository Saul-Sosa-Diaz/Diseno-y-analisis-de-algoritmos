from TSP import TSP
import numpy as np

class greedy(TSP):
  def __init__(self) -> None:
    self.__value = 0
    self.__time = 0
    self.__visited = [False] * 4
  
  def solve(self, matrix):
    value = 0
    actualNode = 0
    self.__visited[0] = True
    while (not all(self.__visited)):
      i = 0
      min = 1000
      index_smallest_element = 0
      while i < len(matrix[actualNode]):
        if matrix[actualNode,i] < min and self.__visited[i] == False:
          min = matrix[actualNode,i]
          index_smallest_element = i
        i += 1

      value += min
      actualNode = index_smallest_element
      self.__visited[actualNode] = True
    
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
    a.solve(v)

  except Exception as e:
    print(str(e))


if __name__ == "__main__":
  main()
