# Let's create tests to check if the code would be running without any errors

from simple_calc import SimpleCalc
import unittest
#import pytest
# importing unittest to inherit TesetCase to create our tests against the code


# unittest.TestCase works with unittest framework as a parent class
class CalcTest(unittest.TestCase):
    calc = SimpleCalc() # creating an object of our SimpleCalc() class

    def test_add(self): #Nameing convention - using test_ in the name of our function will let python interpretor know that this needs to be tested
        # 2 + 2 = 4 outcome is True
        self.assertEqual(self.calc.add(2, 4), 6)
        # this test is checking if 2 + 4 = 6, that would be true, if true the test will pass

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)
        # tests the values as 4 - 2 = 2 to be True if True the test passes

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 2), 4)
        # tests the values as 2 * 2 = 4 to be True if True the test passes

    def test_divide(self):
        self.assertEqual(self.calc.divide(15, 3), 5)
        # tests the values as 15/3 = 5 to be True if True the test passes