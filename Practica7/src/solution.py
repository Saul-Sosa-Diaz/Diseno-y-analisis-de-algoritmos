import numpy as np

class Solution:

  def __init__(self, clusters, centroids, SSE, CPU) -> None:
    self.__clusters = clusters
    self.__centroids = centroids
    self.__SSE = SSE
    self.__CPU = CPU

  def PrintSolution(self):
    for i,cluster in enumerate(0, self.__solution):
      print("Cluster", i, "length:", len(cluster))





def test():
  try:
    a = Solution()
    v = np.array([[0., 25., 10., 15.],
                  [25., 0., 10., 45.],
                  [10., 10., 0., 5.],
                  [15., 45., 5., 0.]])

  except Exception as e:
    print(str(e))


if __name__ == "__main__":
  test()
