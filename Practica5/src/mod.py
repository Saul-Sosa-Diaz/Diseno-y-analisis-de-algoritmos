from DaC import DaC


class BinSearch(DaC):
  '''
  A class that inherits from the DaC class and provides an implementation of the Quick Sort algorithm.
  '''
  def __init__(self, toSearch, size) -> None:
    self.__toSearch = toSearch
    self.__izq = 0
    self.__der = size


  def Small(self, problem: list):
    if isinstance(problem, list):
      return True if len(problem) <= 1 else False
    else:
      return True
    


  def Divide(self, problem: list):
    result = []
    divide = []
    middle = (self.__izq + self.__der) // 2

    if problem[middle] > self.__toSearch:
      for i in range(0, len(problem)):
        if i > middle:
          divide.append(0)
        else:
          divide.append(problem[i])
      self.__der = middle - 1
    elif problem[middle] < self.__toSearch:
      for i in range(0, len(problem)):
        if i < middle:
          divide.append(0)
        else:
          divide.append(problem[i])
      self.__izq = middle + 1
    else:
      divide = middle

    result.append(divide)
    return result

  def SolveSmall(self, problem: list):
    if isinstance(problem, list):
      return -1
    else: 
      return problem

  def Combine(self, s: list):
    return s


def main():
  try:
    v = [1, 2, 1, 3, 65, 567, 456, 423, 2, 324]
    a = BinSearch(567,len(v) - 1)
    
    v.sort()
    print(v)
    print(a.Solve(v))
  except Exception as e:
    print(str(e))


if __name__ == "__main__":
  main()
