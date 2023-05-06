from node import *
from problem import *
from grasp import *
from queue import PriorityQueue


class BranchAndBound:
  def __init__(self, initialLowerBound, problem: Problem, m):
    self.__problem = problem
    self.__m = m
    self.__LowerBound = initialLowerBound
    self.__root = Node(-1, initialLowerBound, [])
    points = problem.GetPoints()
    self.__distanceMatrix = []
    self.__maxDistance = -float('inf')
    self.__maxNumberOfEdges = (m * (m - 1)) / 2
    self.__setOfPoints = set()
    for i in range(0, problem.GetNumOfPoints()):
      self.__setOfPoints.add(i)

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
    self.__solution = []
    self.__nodesGenerated = 1
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
    return round(objetiveValue, 2)



  def bab(self, node: Node):
    nodesToExplore = [node]  # Inicializar la pila con el nodo raíz
    while nodesToExplore:
        # Seleccionar el siguiente nodo hijo de la pila con el mayor valor
        curr_node = max(nodesToExplore)
        nodesToExplore.remove(curr_node)
        if len(curr_node.getAncestors()) == self.__m - 1:  # Si el nodo es una hoja
            ObjetiveValue = self.ObjetiveFunction(curr_node.getAncestors() + [curr_node.getId()]) 
            if ObjetiveValue >= self.__LowerBound: # Update the lower bound
                self.__LowerBound = ObjetiveValue
                self.__solution = curr_node.getAncestors() + [curr_node.getId()]
                for node in nodesToExplore: # Prune the nodes that can't be a solution
                    if node.getupperBound() <= self.__LowerBound:
                        nodesToExplore.remove(node)
            continue
        else:
            childs = []
            # n(n-1)/2 This is used to calculate the number od edges in the graph
            numberOfEdges = self.__maxNumberOfEdges - (len(curr_node.getAncestors()) + 1 * (len(curr_node.getAncestors()))) / 2
            # Crear los nodos hijos del nodo actual
            pointsOutOfSolution = self.__setOfPoints - set(curr_node.getAncestors() + [curr_node.getId()])
            for i in pointsOutOfSolution: 
              if curr_node.getId() == -1:
                  UpperBound = self.ObjetiveFunction(curr_node.getAncestors()) + self.__maxDistance * numberOfEdges
                  newNode = Node(i, UpperBound, curr_node.getAncestors())
              else:
                  UpperBound = self.ObjetiveFunction(curr_node.getAncestors() + [curr_node.getId()]) + self.__maxDistance * numberOfEdges
                  newNode = Node(i, UpperBound, curr_node.getAncestors() + [curr_node.getId()])
                
              if UpperBound > self.__LowerBound:
                childs.append(newNode)
            
            self.__nodesGenerated += len(childs)
            nodesToExplore += childs

    return self.__LowerBound



  def byb_dfs(self, node: Node):
    """
    This function implements the branch and bound algorithm using a depth first search.
    """
    stack = [node]  # initialize stack
    while stack:
        curr_node = stack.pop()  # Select node

        if len(curr_node.getAncestors()) == self.__m - 1:  # Leaf node
            ObjetiveValue = self.ObjetiveFunction(
                curr_node.getAncestors() + [curr_node.getId()])
            if ObjetiveValue >= self.__LowerBound:
                self.__LowerBound = ObjetiveValue
                self.__solution = curr_node.getAncestors() + [curr_node.getId()]
            continue
        else:
            childs = []
            # n(n-1)/2 This is used to calculate the number od edges in the graph
            numberOfEdges = (len(curr_node.getAncestors()) +
                             1 * (len(curr_node.getAncestors()))) / 2
            # Create childs
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
                    if newNode.getupperBound() >= self.__LowerBound:
                      childs.append(newNode)
                      self.__nodesGenerated += len(childs)

            # Add childs to stack in reverse order
            for child in reversed(childs):
                stack.append(child)

        # Prune
        curr_node.setChilds(childs)
        to_remove = []
        for childNode in curr_node.getChilds():
            if childNode.getupperBound() <= self.__LowerBound:
                to_remove.append(childNode)
        for childNode in to_remove:
            curr_node.getChilds().remove(childNode)

    return self.__LowerBound

  def branchAndBound(self):
    startTime = time.perf_counter()
    self.bab(self.__root)
    endTime = time.perf_counter()
    print("Solution: " + str(self.__solution))
    print("Objetive function: " + str(self.ObjetiveFunction(self.__solution)))
    print("Nodes generated: " + str(self.__nodesGenerated))
    print("Time: " + str(endTime - startTime))


def test():
  try:
    problem = Problem(os.path.join(".", "problems", "max_div_15_2.txt"))
    # Greedy
    a = GRASP(problem, 5, 3)

    resultSol, valueObjetive, time = a.Grasp(100)
    print("ya", resultSol, valueObjetive, time)
    branch = BranchAndBound(valueObjetive, problem, 5)
    branch.branchAndBound()

  except Exception as e:
    print(str(e))


if __name__ == "__main__":
  test()
