from functools import total_ordering


class Node:
  def __init__(self, id, upperBound, ancestors):
    self.__id = id
    self.__upperBound = upperBound
    self.__childs = None
    self.__ancestors = ancestors
  
  # Getters and setters
  def setChilds(self, childs):
    self.__childs = childs

  def getChilds(self):
    return self.__childs
  
  def getId(self):
    return self.__id

  def getupperBound(self):
    return self.__upperBound
  
  def __eq__(self, other):
    return self.__upperBound == other.__upperBound

  def __lt__(self, other):
    return self.__upperBound < other.__upperBound
  
  def getAncestors(self):
    return self.__ancestors


  
def test():
  try:
    pass

  except Exception as e:
    print(str(e))


if __name__ == "__main__":
  test()
