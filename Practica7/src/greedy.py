from algorithm import *

class greedy(Algorithm):
  def __init__(self, problem) -> None:
    self.__problem = problem
  
  def Solve():
    """
    1: Seleccionar K puntos como centroides iniciales
    2: repeat
    3: Construir K clusters asignando cada punto al centroide más cercano
    4: Recalcular los centroides de cada cluster
    5: until(Ningún punto cambie de cluster)"""

