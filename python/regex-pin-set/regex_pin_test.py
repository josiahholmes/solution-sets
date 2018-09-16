#!/usr/bin/env python3
import unittest
from regex_pin import *


"""
Codewars: Regex validate PIN Code

ATM machines allow 4 or 6 digit PIN codes and 
PIN codes cannot contain anything but exactly 
4 digits or exactly 6 digits.

If the function is passed a valid PIN string, 
return true, else return false.

eg:

validate_pin("1234") == True
validate_pin("12345") == False
validate_pin("a234") == False
"""


class MyTest(unittest.TestCase):
    def test_regex(self):
        self.assertEqual(validate_pin("1"),False)
        self.assertEqual(validate_pin("12"),False)
        self.assertEqual(validate_pin("123"),False)
        self.assertEqual(validate_pin("1234"), True)
        self.assertEqual(validate_pin("12345"), False)
        self.assertEqual(validate_pin("123456"), True)
        self.assertEqual(validate_pin("a234"), False)
