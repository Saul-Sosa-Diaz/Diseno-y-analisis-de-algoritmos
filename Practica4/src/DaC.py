from install_function import install
from abc import ABC, abstractclassmethod

try:
    import typeguard
except ImportError:
    install('typeguard')
    import typeguard

class DaC(ABC):
    '''
    Abstract class that handles the divide and conquer framwork.
    '''
    def __init__(self) -> None:
      pass

    @typeguard.typechecked
    def Solve(self, problem : list):
      '''
        Solves a problem using the divide and conquer approach.

        :param problem: The problem to solve.
        :type problem: list
        :return: The solution to the problem.
        '''
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
      '''
        Determines whether a problem is small enough to be solved without dividing.

        :param problem: The problem to check.
        :type problem: list
        :return: True if the problem is small enough to be solved without dividing, False otherwise.
        :rtype: bool
        '''
      pass
    
    @abstractclassmethod
    @typeguard.typechecked
    def Divide(self, problem : list):
      '''
        Divides a problem into subproblems.

        :param problem: The problem to divide.
        :type problem: list
        :return: The subproblems.
        :rtype: list of lists
        '''
      pass

    @abstractclassmethod
    @typeguard.typechecked
    def SolveSmall(self, problem : list):
      '''
        Solves a small problem directly, without dividing.

        :param problem: The small problem to solve.
        :type problem: list
        :return: The solution to the small problem.
        '''
      pass

    @abstractclassmethod
    @typeguard.typechecked
    def Combine(self, s1: list, s2: list):
      '''
      Combines the solutions to two subproblems into a solution to the original problem.

      :param s1: The solution to the first subproblem.
      :type s1: list
      :param s2: The solution to the second subproblem.
      :type s2: list
      :return: The combined solution.
      '''
      pass
