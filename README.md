# TDD Test Driven Development
## Why should we use TDD
### What are the benefits of using TDD

**Best Use Cases** 
- We will use pytest unittest in python to implement TDD
- TDD is widely used and is the cheapest way to test the code or implement test driven development

**Best practices for TDD**

- Write the smallest possible test case that matches what we need to program
- TDD cycle starts with everything failing -`Red`
- Write code to pass the test - `Green`
- Refactor the code for next test - `Blue`
- This continues until all the tests have successfully passed


|Method |   Checks that|   New in |
|:---|:---|:---|
|assertEqual(a, b)        | a == b              ||
|assertNotEqual(a, b)     |    a != b              ||  
|assertTrue(x)            |    bool(x) is True     ||  
|assertFalse(x)           |    bool(x) is False    ||  
|assertIs(a, b)           |    a is b             |3.1|
|assertIsNot(a, b)        |    a is not b          |3.1|
|assertIsNone(x)          |    x is None           |3.1|
|assertIsNotNone(x)       |    x is not None       |3.1|
|assertIn(a, b)           |    a in b              |3.1|
|assertNotIn(a, b)        |    a not in b         |3.1|
|assertIsInstance(a, b)   |    isinstance(a, b)    |3.2|
|assertNotIsInstance(a, b)|    not isinstance(a, b)|3.2| 







- Let's create a file called
`test_unittest_simplecalc.py`
  
- Naming convention is extremely important when it comes to TDD in Python
```python
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
```
- Run the tests `python -m pytest`

```python

class SimpleCalc:
    # pass
    def add(self, value1, value2):
        return value1 + value2
        # This function adds the values for value1 and value2 against the test we have in other class

    def subtract(self, value1, value2):
        return value1 - value2


    def multiply(self, value1, value2):
        return value1 * value2

    def divide(self, value1, value2):
        return value1 / value2
```
