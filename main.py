import unittest
import Lab5_Classes
from Lab5_Classes import ECG 
#4 
class testNumbers(unittest.TestCase):
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
        self.assertEqual(self.numbers.factorial(10), 3628800)
        print("Factorial 10 works")
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
        self.assertEqual(self.numbers.stringOfNumber(0), "zero")
        print("String of number 0 works")
        self.assertEqual(self.numbers.stringOfNumber(5), "five")
        print("String of number 5 works")
        self.assertEqual(self.numbers.stringOfNumber(9), "nine")
        print("String of number 9 works")
        with self.assertRaises(ValueError):
            self.numbers.stringOfNumber(10)
        with self.assertRaises(ValueError):
            self.numbers.stringOfNumber(-1)
        with self.assertRaises(TypeError):
            self.numbers.stringOfNumber(3.5)

class TestECG(unittest.TestCase):
    def setUp(self):
        self.ecg = ECG()
        self.sample_ecg = [0.1, 0.2, 1.2, 0.3, 0.1, 1.5, 0.2]

    # 5.1 Test Detect Peaks Function
    def test_detect_peaks(self):
        #With a threshold of 1 the indices should be 2 and 5
        self.assertEqual(self.ecg.detect_peaks(self.sample_ecg, 1), [2, 5])
        print("ECG with threshold of 1 works")
        
        #When the threshold is 3 it shouldn't have any peaks
        self.assertEqual(self.ecg.detect_peaks(self.sample_ecg, 3), [])
        print("ECG with threshold of 3 has no peaks")
    # 5.2 Test remove baseline
    def test_remove_baseline(self):
        cleaned_ecg = self.ecg.remove_baseline(self.sample_ecg)
        
        #Checking that the baseline is about 0
        mean_val = sum(cleaned_ecg) / len(cleaned_ecg)
        self.assertAlmostEqual(mean_val, 0, places=5)
        print("Mean is approximately 0")

    # 5.3 Test Normalization
    def test_normalize(self):
        norm = self.ecg.normalize(self.sample_ecg)

        #Checking normalization keeps max at 1
        self.assertAlmostEqual(max(norm), 1, places=5)
        print("Max of norm is roughly 1")
        
        zero_sig = [0, 0, 0]
        self.assertEqual(self.ecg.normalize(zero_sig), [0, 0, 0])
    
    #Section 7 test heart rate
    def test_heart_rate(self):

        fs = 100
        threshold = 1.0
        
        #getting the peaks
        peaks = self.ecg.detect_peaks(self.sample_ecg, threshold)
        
        #Heart rate checking
        p = self.ecg.detect_peaks(self.sample_ecg, 1.0)
        hr = self.ecg.heart_rate(p, 100)

        bpm = self.ecg.heart_rate(peaks, fs)
        
        self.assertEqual(hr, 2000.0)
        print(f"Sample ECG Heart Rate: {bpm} BPM")

        no_peaks = self.ecg.detect_peaks(self.sample_ecg, 5.0) 
        hr_result = self.ecg.heart_rate(no_peaks, fs)
        self.assertEqual(hr_result, 0)

if __name__ == '__main__':
    unittest.main()
    