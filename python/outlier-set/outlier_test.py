#!/usr/bin/env python3
import unittest
from outlier import *

"""
Codewars: Find the Parity Outlier

You are given an array (which will have a length of 
at least 3, but could be very large) containing integers. 
The array is either entirely comprised of odd integers 
or entirely comprised of even integers except for a 
single integer N. Write a method that takes the array 
as an argument and returns this "outlier" N.

Examples
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)
"""


class MyTest(unittest.TestCase):
    def test_outlier(self):
        self.assertEqual(find_outlier([0, 1, 2]), 1)
        self.assertEqual(find_outlier([1, 2, 3]), 2)
        self.assertEqual(find_outlier([2, 4, 6, 7, 8, 10]), 7)
