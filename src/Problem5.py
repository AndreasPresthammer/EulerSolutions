import unittest
from itertools import count


def is_even_for_all_in_range(low, high, num):
    for i in range(low, high):
        if num % i != 0:
            return False
        
    return True;

def smallestDivided():
    for i in count(200000000, 20):
        if is_even_for_all_in_range(1, 20, i):
            return i

class Test(unittest.TestCase):


    def testName(self):
        expectedVal = 2520
        
        actual = smallestDivided()
        
        self.assertEqual(expectedVal, actual)
    