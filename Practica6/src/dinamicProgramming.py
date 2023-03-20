from TSP import TSP
import numpy as np
import time


class DP(TSP):

  def __init__(self, exceeded=60) -> None:
    self.__value = 0
    self.__time = 0
    self.__path = None
    self.__exceeded = exceeded

  def Solve(self, matrix):
    value = 0
    start_time = time.perf_counter()

    # Distances from B, C and D to A
    gb_0 = matrix[0,1]
    gc_0 = matrix[0,2]
    gd_0 = matrix[0,3]
    
    # Distance from B to A through C or D
    gb_c = matrix[1,2] + gc_0
    gb_d = matrix[1,3] + gd_0
    # Distance from C to A through B or D
    gc_b = matrix[2,1] + gb_0
    gc_d = matrix[2,3] + gd_0
    # Distance from D to A through B or C
    gd_b = matrix[3,1] + gb_0
    gd_c = matrix[3,2] + gc_0

    # Minimum distance from B to A through C and D
    gb_cd = min(matrix[1,2] + gc_d, matrix[1,3] + gd_c)
    # Minimum distance from C to A through B and D
    gc_bd = min(matrix[2,1] + gb_d, matrix[2,3] + gd_b)
    # Minimum distance from D to A through B and C
    gd_bc = min(matrix[3,1] + gb_c, matrix[3,2] + gc_b)

    # Minimum distance from A to A through all B, C and D
    ga_bcd = min(matrix[0, 1] + gb_cd, matrix[0, 2] +
                 gc_bd, matrix[0, 3] + gd_bc)
    # get path
    path = []
    if (matrix[0, 1] + gb_cd < matrix[0, 2] + gc_bd):
      path.insert(0,1)
      if matrix[1, 2] + gc_d < matrix[1, 3] + gd_c:
        path.insert(0, 2)
        path.insert(0, 3)
      else:
        path.insert(0, 3)
        path.insert(0, 2)
    elif(matrix[0, 2] + gc_bd < matrix[0, 3] + gd_bc):
      path.insert(0, 2)
      if matrix[2, 1] + gb_d < matrix[2, 3] + gd_b:
        path.insert(0, 1)
        path.insert(0, 3)
      else:
        path.insert(0, 3)
        path.insert(0, 1)
    else:
      path.insert(0, 3)
      if matrix[3, 1] + gb_c < matrix[3, 2] + gc_b:
        path.insert(0, 1)
        path.insert(0, 2)
      else:
        path.insert(0, 2)
        path.insert(0, 1)

    path.insert(0,0)
    self.__path = path
    end_time = time.perf_counter()
    self.__time = end_time - start_time
    value = ga_bcd
    self.__value = value
    return value



  def Set_exceeded(self, exceeded):
    self.__exceeded = exceeded

  def Get_value(self):
    return self.__value

  def Get_time(self):
    return self.__time

  def Get_path(self):
    return super().Get_path(self.__path)




def main():
  try:
    a = DP()
    v = np.array([[0., 25., 10., 15.],
                  [25., 0., 10., 45.],
                  [10., 10., 0., 5.],
                  [15., 45., 5., 0.]])
    print(a.Solve(v))
    print(a.Get_path())

  except Exception as e:
    print(str(e))


if __name__ == "__main__":
  main()
