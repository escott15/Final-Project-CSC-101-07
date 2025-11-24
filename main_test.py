import unittest 
from main import median_calc

class TestCases(unittest.TestCase):
    def test_median_calc1(self):
        _input = [10, 2, 38, 23, 38, 23, 21]
        expected = 23
        result = median_calc("_",_input)
        self.assertEqual(expected, result)
    
    def test_median_calc2(self):
        _input = [5, 3, 1, 2, 4]
        expected = 3
        result = median_calc("_",_input)
        self.assertEqual(expected, result)
    def test_median_calc3(self):
        _input = 3
        expected = None 
        result = median_calc("_", _input)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()