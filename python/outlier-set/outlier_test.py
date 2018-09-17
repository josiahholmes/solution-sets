#!/usr/bin/env python3
import unittest
from outlier import *


class MyTest(unittest.TestCase):
    def test_outlier(self):
        self.assertEqual(find_outlier([0, 1, 2]), 1)
        self.assertEqual(find_outlier([1, 2, 3]), 2)
        self.assertEqual(find_outlier([2, 4, 6, 7, 8, 10]), 7)
