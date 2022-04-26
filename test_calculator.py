import unittest 
import calculator as calculator
#Test cases to test self methods
#You always create  a child class derived from unittest.TestCase
class TestCalculator(unittest.TestCase):
   #Each test method starts with the keyword test_
  def test_add(self):
    self.assertEqual(calculator.add(4,7), 11)
    self.assertEqual(calculator.add(40,39), 79)
    self.assertEqual(calculator.add(-14,-237), -251)
    self.assertEqual(calculator.add(-15,7), -8)
  def test_subtract(self):
    self.assertEqual(calculator.subtract(10,5), 5)
    self.assertEqual(calculator.subtract(-555,-235), -320)
    self.assertEqual(calculator.subtract(49,-5), 54)
    self.assertEqual(calculator.subtract(70,1000), -930)
  def test_multiply(self):
    self.assertEqual(calculator.multiply(3,7), 21)
    self.assertEqual(calculator.multiply(10,12), 120)
    self.assertEqual(calculator.multiply(3,-18), -54)
    self.assertEqual(calculator.multiply(-3,-30), 90)
  def test_divide(self):
    self.assertEqual(calculator.divide(10,0), "undefined")
    self.assertEqual(calculator.divide(100,2), 50)
    self.assertEqual(calculator.divide(-35,7), -5)
    self.assertEqual(calculator.divide(-10,-2), 5)
# Executing the tests in the above test case class
if __name__ == "__main__":
  unittest.main()
