from abc import ABC, abstractclassmethod
from string import ascii_uppercase

class TSP(ABC):
    '''
    Abstract class that handles the Travelling Salesman Problem.
    '''
      

    @abstractclassmethod
    def Solve(self, problem : list):
      pass


    def Get_path(self,path):
      dict = {k: v for k, v in enumerate(ascii_uppercase)}
      path_string = ""
      for i, node in enumerate(path):
        if i == len(path) - 1:
          path_string += f"{dict[node]}"
        else:
          path_string += f"{dict[node]} -> "
      return path_string
