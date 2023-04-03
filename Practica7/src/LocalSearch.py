from install import install

try:
    import typeguard
except ImportError:
    install('typeguard')
    import typeguard

class LocalSearch:

  @typeguard.typechecked
  def __init__(self, baseSolution : list, numberOfPoints : int) -> None:
    self.__baseSolution = baseSolution
    self.__numberOfClusters = len(baseSolution)
    self.__playground = baseSolution.copy()
    i = 0
    while len(self.__playground) < numberOfPoints:
      if i not in self.__playground:
        self.__playground.append(i)
      i += 1
  
  def GetBaseSolution(self):
    return self.__baseSolution

  def GetNumberOfClusters(self):
    return self.__numberOfClusters
  
  def GetPlayground(self):
    return self.__playground
  
  def Search(self):
    pass

def test():
  try:
    a = LocalSearch([13, 1, 6],15)

    print(a.GetBaseSolution())
    print(a.GetNumberOfClusters())
    print(a.GetPlayground())

  except Exception as e:
    print(str(e))


if __name__ == "__main__":
  test()
