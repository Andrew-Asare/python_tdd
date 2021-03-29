# Let's create tests to check if the code would be running without any errors

from simple_calc import SimpleCalc:
import unittest
#import pytest
# importing unittest to inherit TesetCase to create our tests against the code


# unittest.TestCase works with unittest framework as a parent class
class CalcTest(unittest.TestCase):
    calc = SimpleCalc()

def test_add(self): #Nameing convention - using test_ in the name of our function will let python interpretor know that this needs to be tested
    # 2 + 2 = 4 outcome is True
