from LocalSearch import LocalSearch

class LocalSearchDelete(LocalSearch):
  
  def __init__(self, baseSolution, numberOfPoints) -> None:
    super().__init__(baseSolution, numberOfPoints)
  
  def Search(self):
    baseSolution = self.GetBaseSolution()
    for indexOfSolution, pointOfService in enumerate(baseSolution):
      pointOfService = baseSolution.pop(indexOfSolution)
      # Operacion


      baseSolution.insert(indexOfSolution, pointOfService)


def test():
  try:
    a = LocalSearchDelete([13, 1, 6], 15)

    print(a.GetBaseSolution())
    print(a.GetNumberOfClusters())
    a.Search()

  except Exception as e:
    print(str(e))


if __name__ == "__main__":
  test()
