from LocalSearch import LocalSearch


class LocalSearchInsert(LocalSearch):
  def __init__(self, baseSolution, numberOfPoints) -> None:
    super().__init__(baseSolution, numberOfPoints)

  def Search(self):
    baseSolution = self.GetBaseSolution()
    playground = self.GetPlayground() 
    for element in playground[self.GetNumberOfClusters():]:
      baseSolution.append(element)
      # operaciones

      baseSolution.pop()
      

      


def test():
  try:
    a = LocalSearchInsert([13, 1, 6], 15)

    print(a.GetBaseSolution())
    print(a.GetNumberOfClusters())
    a.Search()

  except Exception as e:
    print(str(e))


if __name__ == "__main__":
  test()
