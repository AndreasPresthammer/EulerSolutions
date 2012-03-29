import unittest

def solution(below):
    # return totalSum(x for x in range(0,below) if x %3 == 0 or x %5 == 0)
    
    totalSum = 0
    for i in range(1, below):
        if i%3 == 0 or i%5 == 0:
            totalSum += i
    return totalSum

class Tests(unittest.TestCase):
    
    def testUpTo10(self):
        result = solution(10)
        self.assertEqual(23, result)
        
    def testUpTo1000(self):
        result = solution(1000)
        
        self.assertEqual(233168, result)