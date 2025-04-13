# https://github.com/sofiagalindo5/lab10-SG-GP.git
# Partner 1: Sofia Galindo
# Partner 2: Gabrielle Polito

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(-1, -1), 0)
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 4), -4)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(multiply(2,0), 0)
        self.assertEqual(multiply(1,9), 9)
        self.assertEqual(multiply(10,10), 100)

    def test_divide(self): # 3 assertions
        self.assertRaises(divide(0, 2), ZeroDivisionError)
        self.assertEqual(divide(1, 3), 3)
        self.assertEqual(divide(2, 4), 2)

    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
        with self.assertRaises(ZeroDivisionError):
            divide(0, 5)
    #     fill in code

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(2, 8), 3)
        self.assertEqual(logarithm(10, 100), 2)
        self.assertEqual(logarithm(2, 2), 1)


    def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            logarithm(8, -2)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)

    def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
        with self.assertRaises(ValueError):
             square_root(-2)
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(100), 10)

    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()