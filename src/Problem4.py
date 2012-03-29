import unittest

def is_palindromic(number):
    originalNum = str(number)
    reversedNum = originalNum[::-1]
    
    return originalNum == reversedNum


def find_largest_3digit_products_that_make_palindrome():
    
    foo = [x*y 
           for x in range(999, 99, -1) 
           for y in range(999, 99, -1) 
           if is_palindromic(x*y)]
    
    return max(foo)

class Test(unittest.TestCase):

    def test_palindromic_123_should_be_false(self):
        self.assertFalse(is_palindromic(123))
        
    def test_palindromic_121_should_be_true(self):
        self.assertTrue(is_palindromic(121))
        
    def testEulerSolution(self):
        print find_largest_3digit_products_that_make_palindrome()
