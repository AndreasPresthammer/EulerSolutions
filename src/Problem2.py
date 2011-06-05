import unittest

def solution(below):
    sum = 0
    prevprev = 0
    prev = 1
    next = 0
    while next < below:
        next = prevprev + prev
        
        if next % 2 == 0:
            sum += next
        
        prevprev = prev
        prev = next
    return sum

class Tests(unittest.TestCase):
    
    def testSimple(self):
        result = solution(89)
        self.assertEqual(44, result)
        
    def testFull(self):
        result = solution(4000000)
        self.assertEqual(4613732, result)
        
