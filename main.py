import unittest
import Lab5_Classes
from Lab5_Classes import ECG 
#4 
class Numbers(unittest.TestCase):
    def setUp(self):
        self.numbers = Lab5_Classes.Numbers()
    #4.1 factorial tests 
    def test_factorial_zero(self):
        self.assertEqual(self.numbers.factorial(0), 1)
        print("Factorial 0 works")
    def test_factorial_one(self):
        self.assertEqual(self.numbers.factorial(1), 1)
        print("Factorial 1 works")
    def test_factorial_large(self):
        self.assertEqual(self.numbers.factorial(100), 3628800)
    def test_factorial_negative(self): 
        with self.assertRaises(ValueError):
            self.numbers.factorial(-1)
    #4.2 addToSum tests
    def test_addToSum_subtractFromSum(self):
        self.numbers.addToSum(5)
        self.assertEqual(self.numbers.sum, 5)
        print("Sum to 5 works")
        self.numbers.addToSum(10)
        self.assertEqual(self.numbers.sum, 15)
        print("Sum to 10 works")
        self.numbers.subtractFromSum(3)
        print("Subtract from sum of 3 works")
        self.assertEqual(self.numbers.sum, 12)
    
    #4.3
    def test_stringOfNumber(self):
        self.assertEqual(self.numbers.stringOfNumbers(0), "zero")
        self.assertEqual(self.numbers.stringOfNumber(5), "five")
        print("String of number 5 works")
        self.assertEqual(self.numbers.stringOfNumber(9), "nine")
        print("String of number 9 works")
        with self.assertRaises(ValueError):
            self.numbers.stringOfNumber(10)
        with self.assertRaises(ValueError):
            self.numbers.stringOfNumber(-1)
        with self.assertRaises(TypeError):
            self.numbers.stringOfNumbers(3.5)

import math
import unittest

class TestNumbers(unittest.TestCase):
    def __init__(self, sum=0):
        self.sum = sum