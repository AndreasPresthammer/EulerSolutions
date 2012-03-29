import unittest
import operator
# lrange stolen from http://stackoverflow.com/questions/2187135/python-range-and-xrange-for-13-digit-numbers
def lrange(num1, num2 = None, step = 1):
    op = operator.__lt__

    if num2 is None:
        num1, num2 = 0, num1
    if num2 < num1:
        if step > 0:
            num1 = num2
        op = operator.__gt__
    elif step < 0:
        num1 = num2

    while op(num1, num2):
        yield num1
        num1 += step

def getFactors(number):
    n = number
    for i in lrange(2, n + 1):
        print i
        
        while(n % i == 0):
            yield i
            n /= i
        
        if n == 1:
            break
        
class Tests(unittest.TestCase):
    
    def testEulerSolution(self):
        number = 600851475143
        
        print list(getFactors(number))
    
#    def testPrimeFactorization1(self):
#        number = 13195
#        expectedFactors = [5,7,13,29]
#        
#        self.assertEqual(expectedFactors, list(getFactors(number)))
#
#    def testNumberIsPrime_5_ShouldReturn_5(self):
#        expectedFactors = [5]
#        
#        self.assertEqual(expectedFactors, list(getFactors(5)))
#        
#    def testNumberIsPrime_4_ShouldReturn_2x2(self):
#        expectedFactors = [2, 2]
#        
#        self.assertEqual(expectedFactors, list(getFactors(4)))
