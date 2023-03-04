import unittest
from mergeSort import MergeSort
from quickSort import QuickSort

class TestSortMethods(unittest.TestCase):
    
    def setUp(self) -> None: 
      self.__v1 = [78, 49, 694, 26, 297, 798, 634, 748, 569, 846]
      self.__v2 = [650, 330, 128, 369, 93, 439, 438, 815, 589, 624]
      self.__v3 = [-584, 47, 310, -716, -525, 324, 238, 192, 268, -968]
      self.__v4 = [1, 1, 1, 1]
      self.__v_empty = []
      self.__v_error = 7
    
    def test_quickSort(self) -> None:
      vector = QuickSort()
      self.assertEqual(vector.Solve(self.__v1), sorted(self.__v1))
      self.assertEqual(vector.Solve(self.__v2), sorted(self.__v2))
      self.assertEqual(vector.Solve(self.__v3), sorted(self.__v3))
      self.assertEqual(vector.Solve(self.__v4), sorted(self.__v4))
      self.assertEqual(vector.Solve(self.__v_empty), [])
      with self.assertRaises(Exception):
        vector.Solve(self.__v_error)

    def test_mergeSort(self):
      vector = MergeSort()
      self.assertEqual(vector.Solve(self.__v1), sorted(self.__v1))
      self.assertEqual(vector.Solve(self.__v2), sorted(self.__v2))
      self.assertEqual(vector.Solve(self.__v3), sorted(self.__v3))
      self.assertEqual(vector.Solve(self.__v4), sorted(self.__v4))
      self.assertEqual(vector.Solve(self.__v_empty), [])
      with self.assertRaises(Exception):
        vector.Solve(self.__v_error)


if __name__ == '__main__':
    unittest.main()
