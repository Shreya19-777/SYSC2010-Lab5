import unittest
import Lab5_Classes
from Lab5_Classes import ECG 
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

class TestECG(unittest.TestCase):
    def setUp(self):
        self.ecg = ECG()
        self.sample_ecg = [0.1, 0.2, 1.2, 0.3, 0.1, 1.5, 0.2]

    # 5.1 Test Detect Peaks Function
    def test_detect_peaks(self):
        #With a threshold of 1 the indices should be 2 and 5
        self.assertEqual(self.ecg.detect_peaks(self.sample_ecg, 1), [2, 5])
        
        #When the threshold is 3 it shouldn't have any peaks
        self.assertEqual(self.ecg.detect_peaks(self.sample_ecg, 3), [])
        
    # 5.2 Test remove baseline
    def test_remove_baseline(self):
        cleaned_ecg = self.ecg.remove_baseline(self.sample_ecg)
        
        #Checking that the baseline is about 0
        mean_val = sum(cleaned_ecg) / len(cleaned_ecg)
        self.assertAlmostEqual(mean_val, 0, places=7)

    # 5.3 Test Normalization
    def test_normalize(self):
        norm = self.ecg.normalize(self.sample_ecg)
        
        #Checking normalization keeps max at 1
        self.assertEqual(max(norm), 1)
        
        zero_sig = [0, 0, 0]
        self.assertEqual(self.ecg.normalize(zero_sig), [0, 0, 0])

if __name__ == '__main__':
    unittest.main()
    