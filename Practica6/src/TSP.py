from abc import ABC, abstractclassmethod
import time 

class TSP(ABC):
    '''
    Abstract class that handles the Travelling Salesman Problem.
    '''
    def __init__(self) -> None:
      pass

    @abstractclassmethod
    def solve(self, problem : list):
      pass
