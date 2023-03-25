import numpy as np

class Solution:

  def __init__(self) -> None:
    pass




def main():
  try:
    a = Solution()
    v = np.array([[0., 25., 10., 15.],
                  [25., 0., 10., 45.],
                  [10., 10., 0., 5.],
                  [15., 45., 5., 0.]])

  except Exception as e:
    print(str(e))


if __name__ == "__main__":
  main()
