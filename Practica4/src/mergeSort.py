from DaC import DaC

class MergeSort(DaC):
  def Small(self, problem: list):
    return True if len(problem) <= 2 else False

  def Divide(self, problem: list):
    result = []
    divide1 = []
    divide2 = []
    for i in range(0, len(problem)//2):
      divide1.append(problem[i])
    result.append(divide1)

    for i in range(len(problem)//2, len(problem)):
      divide2.append(problem[i])
    result.append(divide2)

    return result

  def SolveSmall(self, problem: list):
    if (len(problem) == 2):
      if (problem[0] > problem[1]):
        aux = problem[0]
        problem[0] = problem[1]
        problem[1] = aux
    return problem

  def Combine(self, s1: list, s2: list):
    result = [0] * (len(s1)+len(s2))
    i = 0
    j = 0
    for k in range(0, len(s1)+len(s2)):
      if i >= len(s1):
        while j < len(s2):
          result[k] = s2[j]
          j += 1
          k += 1
        break
      elif j >= len(s2):
        while i < len(s1):
          result[k] = s1[i]
          i += 1
          k += 1
        break
      elif s1[i] < s2[j]:
        result[k] = s1[i]
        i += 1
      else:
        result[k] = s2[j]
        j += 1
    return result


def main():
  try:
    a = MergeSort()
    v = [78, 49, 694, 26, 297, 798, 634, 748, 569, 846]
    print(a.Solve(v))
  except Exception as e:
    print(str(e))



if __name__ == "__main__":
  main()
