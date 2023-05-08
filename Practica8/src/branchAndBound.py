from node import *
from problem import *
from grasp import *


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

    self.__solution = []
    self.__nodesGenerated = 1




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



  def bab(self, node: Node):
    nodesToExplore = [node]  # Inicializar la pila con el nodo raíz
    while nodesToExplore:
        # Seleccionar el siguiente nodo hijo de la pila con el mayor valor
        curr_node = min(nodesToExplore)
        nodesToExplore.remove(curr_node)

        if len(curr_node.getAncestors()) == self.__m - 1:  # Si el nodo es una hoja
            ObjetiveValue = self.ObjetiveFunction(curr_node.getAncestors() + [curr_node.getId()]) 
            if round(ObjetiveValue, 5) >= round(self.__LowerBound, 5): # Update the lower bound
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
            k = 1
            if curr_node.getId() == -1:
               k = 0
            for i in range(curr_node.getId() + 1, self.__problem.GetNumOfPoints() - 1 - (self.__m - (len(curr_node.getAncestors()) + k)) + 1):
              if curr_node.getId() == -1:
                  UpperBound = self.ObjetiveFunction(curr_node.getAncestors()) + self.__maxDistance * numberOfEdges
                  newNode = Node(i, UpperBound, curr_node.getAncestors())
              else:
                  UpperBound = self.ObjetiveFunction(curr_node.getAncestors() + [curr_node.getId()]) + self.__maxDistance * numberOfEdges
                  newNode = Node(i, UpperBound, curr_node.getAncestors() + [curr_node.getId()])
                
              if UpperBound >= self.__LowerBound:
                childs.append(newNode)
            
            self.__nodesGenerated += len(childs)
            nodesToExplore += childs

    return self.__LowerBound



  def bab_dfs(self, node: Node):
    """
    This function implements the branch and bound algorithm using a depth first search.
    """
    stack = [node]  # initialize stack
    while stack:
        curr_node = stack.pop()  # Select node
        if len(curr_node.getAncestors()) == self.__m - 1:  # Si el nodo es una hoja
              ObjetiveValue = self.ObjetiveFunction(curr_node.getAncestors() + [curr_node.getId()]) 
              if ObjetiveValue >= self.__LowerBound: # Update the lower bound
                  self.__LowerBound = ObjetiveValue
                  self.__solution = curr_node.getAncestors() + [curr_node.getId()]
                  for node in stack: # Prune the nodes that can't be a solution
                      if node.getupperBound() <= self.__LowerBound:
                          stack.remove(node)
              continue
        else:
            childs = []
            # n(n-1)/2 This is used to calculate the number od edges in the graph
            numberOfEdges = self.__maxNumberOfEdges - (len(curr_node.getAncestors()) + 1 * (len(curr_node.getAncestors()))) / 2
            # Crear los nodos hijos del nodo actual
            for i in range(0, self.__problem.GetNumOfPoints() - (self.__m-len(curr_node.getAncestors()) + 1)):
              if i not in curr_node.getAncestors() + [curr_node.getId()]:
                if curr_node.getId() == -1:
                    UpperBound = self.ObjetiveFunction(curr_node.getAncestors()) + self.__maxDistance * numberOfEdges
                    newNode = Node(i, UpperBound, curr_node.getAncestors())
                else:
                    UpperBound = self.ObjetiveFunction(curr_node.getAncestors() + [curr_node.getId()]) + self.__maxDistance * numberOfEdges
                    newNode = Node(i, UpperBound, curr_node.getAncestors() + [curr_node.getId()])
                  
                if UpperBound >= self.__LowerBound:
                  childs.append(newNode)

            self.__nodesGenerated += len(childs)
            # Add childs to stack in reverse order
            for child in reversed(childs):
                stack.append(child)

    return self.__LowerBound




  def BranchAndBound(self):
    startTime = time.perf_counter()
    self.bab(self.__root)
    endTime = time.perf_counter()
    return self.__solution, self.__LowerBound, self.__nodesGenerated, round(endTime - startTime, 4)
    




def test():
  try:
    problem = Problem(os.path.join(".", "problems", "max_div_30_3.txt"))
    # Greedy
    a = GRASP(problem, 5, 3)

    resultSol, valueObjetive, time = a.Grasp(100)
    print(resultSol, valueObjetive, time)
    branch = BranchAndBound(valueObjetive, problem, 5)
    print(branch.BranchAndBound())
  except Exception as e:
    print(str(e))


if __name__ == "__main__":
  test()
