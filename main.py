import unittest
import Lab5_Classes
#4 
class Numbers(unittest.TestCase):
    def setUp(self):
        self.numbers = Numbers()
    #4.1 factorial tests 
    def test_factorial_zero(self):
        self.assertEqual(self.numbers.factorial(0), 1)
    def test_factorial_one(self):
        self.assertEqual(self.numbers.factorial(1), 1)
    def test_factorial_large(self):
        self.assertEqual(self.numbers.factorial(100), 3628800)
    def test_factorial_negative(self): 
        with self.assertRaises(ValueError):
            self.numbers.factorial(-1)
    #4.2 addToSum tests
    def test_addToSum_subtractFromSum(self):
        self.numbers.addToSum(5)
        self.assertEqual(self.numbers.sum, 5)
        self.numbers.addToSum(10)
        self.assertEqual(self.numbers.sum, 15)
        self.numbers.subtractFromSum(3)
        self.assertEqual(self.numbers.sum, 12)
    
    #4.3
    def test_stringOfNumber(self):
        self.assertEqual(self.numbers.stringOfNumbers(0), "zero")
        self.assertEqual(self.numbers.stringOfNumber(5), "five")
        self.assertEqual(self.numbers.stringOfNumber(9), "nine")
        with self.assertRaises(ValueError):
            self.numbers.stringOfNumbers(10)
        with self.assertRaises(ValueError):
            self.numbers.stringOfNumbers(-1)
        with self.assertRaises(TypeError):
            self.numbers.stringOfNumbers(3.5)

import math
import unittest

class TestNumbers(unittest.TestCase):
    def __init__(self, sum=0):
        self.sum = sum