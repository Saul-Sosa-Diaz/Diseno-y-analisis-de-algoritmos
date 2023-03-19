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
      solutions = []
      for i in r:
        solutions.append(self.Solve(i))
      t = self.Combine(solutions)
      return t
 
    @abstractclassmethod
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
    def SolveSmall(self, problem : list):
      '''
        Solves a small problem directly, without dividing.

        :param problem: The small problem to solve.
        :type problem: list
        :return: The solution to the small problem.
        '''
      pass

    @abstractclassmethod
    def Combine(self, s: list):
      '''
      Combines the solutions to two subproblems into a solution to the original problem.

      :param s: The solution to the first subproblem.
      :type s: list
      :return: The combined solution.
      '''
      pass
