from DaC import DaC

class MergeSort(DaC):
  '''
  A class that inherits from the DaC class and provides an implementation of the Merge Sort algorithm.
  '''
  def Small(self, problem: list):
    return True if len(problem) <= 1 else False



  def Divide(self, problem: list):
    '''
    Splits the list "problem" into two approximately equal sublists and returns a list of two sublists.

    :param problem: A list that will be divided into two sublists.
    :type problem: list
    :return: A list of two sublists, the first with the first half of the original list and the second with the second half of the original list.
    :rtype: list
    '''
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
    return problem



  def Combine(self, s):
    '''
    Combines two sorted lists, s, into a single sorted list and returns it.

    :param s: The first sorted list to be combined.
    :type s: list
    :return: A sorted list that contains all the elements of s.
    :rtype: list
    '''

    result = [0] * (len(s[0])+len(s[1]))
    i = 0
    j = 0
    for k in range(0, len(s[0])+len(s[1])):
      # The first list is finished
      if i >= len(s[0]):
        # As long as there are still items in the second list, they are added to the resulting list.
        while j < len(s[1]):
          result[k] = s[1][j]
          j += 1
          k += 1
        break

      # The second list is finished
      elif j >= len(s[1]):
        # As long as there are still items in the fist list, they are added to the resulting list.
        while i < len(s[0]):
          result[k] = s[0][i]
          i += 1
          k += 1
        break

      # Put the smaller of the two elements in the resulting list, then move up one position
      elif s[0][i] < s[1][j]:
        result[k] = s[0][i]
        i += 1
      else:
        result[k] = s[1][j]
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
