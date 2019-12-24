'''
Created on 16-Mar-2019

@author: VNSquare Tech
'''
import unittest
from UniTesting.arithmetic import add

class ArithmeticTest(unittest.TestCase):
    
    def test_add(self):
        sum = add(10,20)
        self.assertEquals(sum,30)