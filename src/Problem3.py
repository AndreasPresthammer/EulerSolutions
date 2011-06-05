import unittest
import math

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

def findPrime(number):
    for i in range(3, math.sqrt(number)):
        if i%2==0:
            yield i

class Tests(unittest.TestCase):
    
    def testSimple(self):
        for item in findPrime(10):
            print item
#        result = solution(13195)
#        self.assertEqual(29, result)
        
#    def testFull(self):
#        result = solution(4000000)
#        self.assertEqual(4613732, result)
        
