from install_function import install
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
    def Solve(self, problem : list):
      if self.Small(problem):
        return self.SolveSmall(problem)
      r = self.Divide(problem)
      s1 = self.Solve(r[0])
      s2 = self.Solve(r[1])
      t = self.Combine(s1,s2)
      return t
 
    @abstractclassmethod
    @typeguard.typechecked
    def Small(self, problem : list):
      pass
    
    @abstractclassmethod
    @typeguard.typechecked
    def Divide(self, problem : list):
      pass

    @abstractclassmethod
    @typeguard.typechecked
    def SolveSmall(self, problem : list):
      pass

    @abstractclassmethod
    @typeguard.typechecked
    def Combine(self, s1: list, s2: list):
      pass
