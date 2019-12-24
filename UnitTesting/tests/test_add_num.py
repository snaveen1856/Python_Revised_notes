'''
Created on Oct 30, 2019

@author: madhu
'''
import unittest
from arithmetic.add_num import add
class AddNumTest(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def test_add(self):
        n1 = 10
        n2 = 20
        res = add(n1,n2)
        self.assertEqual(32, res, "Actual value is wrong")
 
    def test_sub(self):
        pass
    
    def test_mul(self):
        pass
    
    def test_div(self):
        pass
if __name__ == "__main__":
    unittest.main()