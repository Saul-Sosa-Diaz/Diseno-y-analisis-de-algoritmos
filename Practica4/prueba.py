from utils import install
from abc import ABC, abstractclassmethod 

try:
    import typeguard
except ImportError:
    install('typeguard')
    import typeguard

class DaC(ABC):

    def __init__(self) -> None:
      pass

    @typeguard.typechecked
    def Solve(self, problem : list , n : int ):
      if self.Small(problem):
        return self.SolveSmall(problem)
      r = self.Divide(problem, n)
      s1 = self.Solve(r[0], n//2)
      s2 = self.Solve(r[1], n//2)
      t = self.Combine(s1,s2)
      return t
 
    @abstractclassmethod
    @typeguard.typechecked
    def Small(self, problem : list):
      pass
    
    @abstractclassmethod
    @typeguard.typechecked
    def Divide(self, problem : list, n : int):
      pass

    @abstractclassmethod
    @typeguard.typechecked
    def SolveSmall(self, problem : list):
      pass

    @abstractclassmethod
    @typeguard.typechecked
    def Combine(self, s1: list, s2: list):
      pass


class MergeSort(DaC):
   
  def Small(self, problem: list):
    return True if len(problem) <= 2 else False
    
  def Divide(self, problem: list, n: int):
    result = []
    divide1 = []
    divide2 = []
    for i in range(0,len(problem)//2):
      divide1.append(problem[i])
    result.append(divide1)
    for i in range(len(problem)//2, len(problem)):
      divide2.append(problem[i])
    result.append(divide2)
  
    return result
    
  def SolveSmall(self, problem: list):
    if (len(problem) == 2):
      if (problem[0] > problem[1]):
        aux = problem[0]
        problem[0] = problem[1]
        problem[1] = aux
    return problem
    
  def Combine(self, s1: list, s2: list):
    result = [0] * (len(s1)+len(s2))
    i = 0
    j = 0
    for k in range(0, len(s1)+len(s2)):
      if  i >= len(s1):
        while j < len(s2):
          result[k] = s2[j]
          j += 1
          k += 1
        break
      elif j >= len(s2):
        while i < len(s1):
          result[k] = s1[i]
          i += 1
          k += 1
        break
      elif s1[i] < s2[j]:
        result[k] = s1[i]
        i += 1
      else:
        result[k] = s2[j]
        j += 1
    return result

    
   
a = MergeSort()
v = [847, 166, 525, 342, 839, 965, 159, 961, 414, 337]
print(a.Solve(v,len(v)))