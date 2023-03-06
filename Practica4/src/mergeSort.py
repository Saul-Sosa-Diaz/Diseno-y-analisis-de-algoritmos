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



  def Combine(self, s1: list, s2: list):
    '''
    Combines two sorted lists, s1 and s2, into a single sorted list and returns it.

    :param s1: The first sorted list to be combined.
    :type s1: list
    :param s2: The second sorted list to be combined.
    :type s2: list
    :return: A sorted list that contains all the elements of s1 and s2.
    :rtype: list
    '''

    result = [0] * (len(s1)+len(s2))
    i = 0
    j = 0
    for k in range(0, len(s1)+len(s2)):
      # The first list is finished
      if i >= len(s1):
        # As long as there are still items in the second list, they are added to the resulting list.
        while j < len(s2):
          result[k] = s2[j]
          j += 1
          k += 1
        break

      # The second list is finished
      elif j >= len(s2):
        # As long as there are still items in the fist list, they are added to the resulting list.
        while i < len(s1):
          result[k] = s1[i]
          i += 1
          k += 1
        break

      # Put the smaller of the two elements in the resulting list, then move up one position
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
