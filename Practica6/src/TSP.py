from abc import ABC, abstractclassmethod
import time 

class TSP(ABC):
    '''
    Abstract class that handles the Travelling Salesman Problem.
    '''
      

    @abstractclassmethod
    def Solve(self, problem : list):
      pass


    def Get_path(self,path):
      dict = {0: "A",
              1: "B",
              2: "C",
              3: "D"}
      path_string = ""
      for i, node in enumerate(path):
        if i == len(path) - 1:
          path_string += f"{dict[node]}"
        else:
          path_string += f"{dict[node]} -> "
      return path_string
