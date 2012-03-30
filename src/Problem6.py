import unittest


class Test(unittest.TestCase):


    def testName(self):
        sumOfSquares = sum([x ** 2 for x in range(1, 101)])
        print sumOfSquares
        
        squareOfSums = sum([x for x in range(1, 101)]) ** 2
        print squareOfSums
        
        diff  = squareOfSums - sumOfSquares
        print diff
