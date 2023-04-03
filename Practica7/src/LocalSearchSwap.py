from LocalSearch import LocalSearch


class LocalSearchSwap(LocalSearch):
  def __init__(self, baseSolution, numberOfPoints) -> None:
    super().__init__(baseSolution, numberOfPoints)
  
  def Search(self):
    baseSolution = self.GetBaseSolution()
    playground = self.GetPlayground() 
    for element in playground[self.GetNumberOfClusters():]:
      for indexOfSolution, pointOfService in enumerate(baseSolution):
        pointOfService = baseSolution.pop(indexOfSolution)
        baseSolution.insert(indexOfSolution, element)
        # Operacion
        
        baseSolution.pop(indexOfSolution)
        baseSolution.insert(indexOfSolution, pointOfService)



def test():
  try:
    a = LocalSearchSwap([13, 1, 6], 15)

    print(a.GetBaseSolution())
    print(a.GetNumberOfClusters())
    a.Search()

  except Exception as e:
    print(str(e))


if __name__ == "__main__":
  test()
