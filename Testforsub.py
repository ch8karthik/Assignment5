#!/usr/bin/python3
# Test case for subtracting two numbers
import unittest

from Prog1 import subtraction

class TestSub(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to subtract two numbers
        """
        a = 32
        b = 23
        result = subtraction(a,b)
        self.assertEqual(result, 55)

if __name__ == '__main__':
    unittest.main()