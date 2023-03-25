from colors import bcolors
from install import install
import math
from abc import ABC, abstractclassmethod

try:
    import typeguard
except ImportError:
    install('typeguard')
    import typeguard


class Algorithm(ABC):
    def __init__(self) -> None:
        pass

    @typeguard.typechecked
    def EuclideanDistance(self, p1 : list, p2 : list):
      # Verify that the points belong to the same vector space
      if len(p1) != len(p2):
         raise Exception(bcolors.FAIL + 
                         "Error in EuclideanDistance -> The points must have the same dimensions." + bcolors.ENDC + 
                         "\nLength of p1: " + str(len(p1)) + "\nLength of p2: " + str(len(p2)))
     
      acc = 0
      for i in range(0, len(p1)):
        acc += (p1[i]-p2[i])**2
      acc = math.sqrt(acc)
      return acc


def main():
  try:
    a = Algorithm()
    p1 = [7.8, 0.1, 6.6]
    p2 = [9.2, 1.2, 9.7]
    print(a.EuclideanDistance(p1,p2))

  except Exception as e:
    print(str(e))


if __name__ == "__main__":
  main()
