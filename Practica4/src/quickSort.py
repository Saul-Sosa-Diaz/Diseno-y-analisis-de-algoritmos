from DaC import DaC

class QuickSort(DaC):
  '''
  A class that inherits from the DaC class and provides an implementation of the Quick Sort algorithm.
  '''
  def Small(self, problem: list):
    return True if len(problem) <= 1 else False



  def Divide(self, problem: list):
    '''
    Divide a problem into two smaller problems based on a pivot element.
    
    :param problem: A list of integers representing the problem to be divided.
    :type problem: list
    :return: A list of two lists representing the smaller problems.
    :rtype: list
    '''
    result = []
    divide1 = []
    divide2 = []
    pivot = problem[len(problem) - 1]
    i = 0
    r = len(problem) - 1
    while i < r:
      while problem[i] <= pivot and i < r:
        i += 1
      while problem[r] >= pivot and i < r:
        r -= 1

      if (i > r):
        break
      # swap
      aux = problem[i]
      problem[i] = problem[r]
      problem[r] = aux

    # swap
    aux = problem[i]
    problem[i] = problem[len(problem) - 1]
    problem[len(problem) - 1] = aux
    # If the problem only has 2 elements and are equal.
    if r <= 0 and len(problem) == 2:
      divide1 = [problem[0]]
      divide2 = [problem[1]]
    else:  
      divide1 = problem[:r]
      divide2 = problem[r:]
    result.append(divide1)
    result.append(divide2)

    return result

  def SolveSmall(self, problem: list):
    return problem


  def Combine(self, s1: list):
    result = []
    for i in s1:
      result += i
    return result

def main():
  try:
    a = QuickSort()
    v = [1,2,1,3,65,567,456,423,2,324]
    print(a.Solve(v))
  except Exception as e:
    print(str(e))


if __name__ == "__main__":
  main()
