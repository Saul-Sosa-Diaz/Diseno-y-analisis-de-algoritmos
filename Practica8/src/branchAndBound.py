from node import *
from problem import *
from grasp import *


class BranchAndBound:
  def __init__(self, initialLowerBound, problem : Problem, m):
    self.__problem = problem
    self.__m = m
    self.__LowerBound = initialLowerBound
    self.__root = Node(-1, initialLowerBound, [])
    points = problem.GetPoints()
    self.__distanceMatrix = []
    self.__maxDistance = -float('inf')
    
    for i in range(0, len(points)):
      row = []
      for j in range(0, len(points)):
        if j == i:
          row.append(float('inf'))
        elif j < i:
          distance = self.EuclideanDistance(points[j], points[i])
          if self.__maxDistance < distance:
            self.__maxDistance = distance
          row.append(distance)
        else:
          row.append(self.EuclideanDistance(points[i], points[j]))
      self.__distanceMatrix.append(row)

    childs = []
    self.__expandedNodes = []
    for i in range(0, self.__problem.GetNumOfPoints()):
      node = Node(i, self.__maxDistance, None)
      childs.append(node)

    self.__root.setChilds(childs)


  def EuclideanDistance(self, p1: list, p2: list):
      '''
        This function calculates the Euclidean distance between two points in a vector space.
        Args:
            p1 (list): List representing the first point.
            p2 (list): List representing the second point.
        Returns:
            float: The Euclidean distance between the two points.
        Raises:
            Exception: If the two points do not have the same number of dimensions.
      '''
      # Verify that the points belong to the same vector space
      if len(p1) != len(p2):
         raise Exception(bcolors.FAIL +
                         "Error in EuclideanDistance -> The points must have the same dimensions." + bcolors.ENDC +
                         "\nLength of p1: " + str(len(p1)) + "\nLength of p2: " + str(len(p2)))

      acc = 0
      for i in range(0, len(p1)):
        acc += (p1[i]-p2[i])**2
      acc = math.sqrt(acc)
      return acc



  def ObjetiveFunction(self, solution):
    objetiveValue = 0
    for i in range(0, len(solution)):
      for j in range(i + 1, len(solution)):
        objetiveValue += self.__distanceMatrix[solution[i]][solution[j]]
    return objetiveValue

      
  def byb_dfs(self, node: Node):
    stack = [node]  # Inicializar la pila con el nodo raíz
    while stack:
        curr_node = stack.pop()  # Seleccionar el siguiente nodo hijo de la pila
        if len(curr_node.getAncestors()) == self.__m - 1:  # Si el nodo es una hoja
            ObjetiveValue = self.ObjetiveFunction(
                curr_node.getAncestors() + [curr_node.getId()])
            if ObjetiveValue >= self.__LowerBound:
                self.__LowerBound = ObjetiveValue
                self.__expandedNodes = curr_node.getAncestors() + \
                    [curr_node.getId()]
            continue
        else:
            childs = []
            # n(n-1)/2 This is used to calculate the number od edges in the graph
            numberOfEdges = (len(curr_node.getAncestors()) +
                             1 * (len(curr_node.getAncestors()))) / 2
            # Crear los nodos hijos del nodo actual
            for i in range(0, self.__problem.GetNumOfPoints()):
                if i not in curr_node.getAncestors() + [curr_node.getId()]:
                    if curr_node.getId() == -1:
                        UpperBound = self.ObjetiveFunction(
                            curr_node.getAncestors()) + self.__maxDistance * numberOfEdges
                        newNode = Node(i, UpperBound, curr_node.getAncestors())
                    else:
                        UpperBound = self.ObjetiveFunction(curr_node.getAncestors(
                        ) + [curr_node.getId()]) + self.__maxDistance * numberOfEdges
                        newNode = Node(
                            i, UpperBound, curr_node.getAncestors() + [curr_node.getId()])
                    childs.append(newNode)
            # Agregar los nodos hijos a la pila en orden inverso
            for child in reversed(childs):
                stack.append(child)

        # Podar los nodos hijos no prometedores
        curr_node.setChilds(childs)
        to_remove = []
        for childNode in curr_node.getChilds():
            if childNode.getupperBound() <= self.__LowerBound:
                to_remove.append(childNode)
        for childNode in to_remove:
            curr_node.getChilds().remove(childNode)

    return self.__LowerBound

      



  def branchAndBound(self):
    self.byb_dfs(self.__root)
    print("Expanded nodes: " + str(self.__expandedNodes))
    print("Objetive function: " + str(self.ObjetiveFunction(self.__expandedNodes)))
   



def test():
  try:
    problem = Problem(os.path.join(".", "problems", "max_div_15_2.txt"))
    # Greedy
    a = GRASP(problem, 3, 3)
    resultSol, valueObjetive,time = a.Grasp(1)
    branch = BranchAndBound(valueObjetive, problem, 3)
    branch.branchAndBound()

  except Exception as e:
    print(str(e))


if __name__ == "__main__":
  test()