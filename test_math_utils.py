import unittest
from math_utils import add, subtract

class TestMathUtils(unnitest.TestCase:
  def test_add(self):
    self.assertEqual(add(5,5), 10)
    self.assertEqual(add(1,-1), 0)

  def test_subtract(self):
    self.assertEqual(add(10,5), 5)
    self.assertEqual(add(1-,-1), 0)

if __name__ == '__main__':
    unittest.main()
