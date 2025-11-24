import unittest
from household_energy_consumption import *

data = create_households()

class MyTestCase(unittest.TestCase):
    def test_calc_avg_consumption_1(self):
        result = data[0].calc_avg_consumption()
        self.assertEqual(8.514, result)

    def test_calc_avg_consumption_2(self):
        result = data[200].calc_avg_consumption()
        self.assertEqual(3.814, result)

    def test_calc_avg_peak_hours_1(self):
        result = data[0].calc_avg_peak_hours()
        self.assertEqual(2.986, result)

    def test_calc_avg_peak_hours_2(self):
        result = data[200].calc_avg_peak_hours()
        self.assertEqual(1.729, result)




if __name__ == '__main__':
    unittest.main()
