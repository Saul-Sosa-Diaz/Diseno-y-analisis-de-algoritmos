from DaC import DaC

class QuickSort(DaC):
  def Small(self, problem: list):
    return True if len(problem) <= 2 else False

  def Divide(self, problem: list):
    result = []
    divide1 = []
    divide2 = []
    pivot = problem[len(problem) - 1]
    i = 0
    r = len(problem) - 1

    if all(elem == problem[0] for elem in problem):
        result.append(problem)
        result.append([])
        return result

    while i < r:
      while problem[i] < pivot:
        i += 1
      while problem[r] > pivot:
        r -= 1
      if (i > r):
        break
      # swap
      aux = problem[i]
      problem[i] = problem[r]
      problem[r] = aux
      


    divide1 = problem[:r]
    divide2 = problem[r:]
    result.append(divide1)
    result.append(divide2)

    return result

  def SolveSmall(self, problem: list):
    return problem

  def Combine(self, s1: list, s2: list):
    result = s1 + s2
    return result


def main():
  try:
    a = QuickSort()
    v = [1,2,1,3]
    print(a.Solve(v))
  except Exception as e:
    print(str(e))


if __name__ == "__main__":
  main()
