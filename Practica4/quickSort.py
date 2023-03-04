from DaC import DaC

class QuickSort(DaC):
  def Small(self, problem: list):
    return True if len(problem) == 1 else False

  def Divide(self, problem: list):
    result = []
    divide1 = []
    divide2 = []
    pivot = problem[len(problem) - 1]
    i = 0
    r = len(problem) - 1

    while True:
      while problem[i] < pivot:
        i += 1
      while problem[r] > pivot:
        r -= 1
      if (i >= r):
        break
      # swap
      aux = problem[i]
      problem[i] = problem[r]
      problem[r] = aux

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
  a = QuickSort()
  v = [847, 166, 525, 342, 839, 965, 159, 961, 414, 337]
  print(a.Solve(v))


if __name__ == "__main__":
  main()
