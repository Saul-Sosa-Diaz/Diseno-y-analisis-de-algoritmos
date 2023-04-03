from LocalSearch import LocalSearch


class LocalSearchSwap(LocalSearch):
  def __init__(self, baseSolution, numberOfPoints) -> None:
    super().__init__(baseSolution, numberOfPoints)
  
  def Search(self):
    pass


def test():
  try:
    a = LocalSearchSwap([13, 1, 6], 15)

    print(a.GetBaseSolution())
    print(a.GetNumberOfClusters())
    print(a.GetPlayground())

  except Exception as e:
    print(str(e))


if __name__ == "__main__":
  test()
