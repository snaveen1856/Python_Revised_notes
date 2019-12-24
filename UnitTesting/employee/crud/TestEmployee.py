'''
Created on 02-Feb-2019

@author: VNSquare Tech
'''
from employee.crud.Employee import Employee
import unittest

class TestEmployee(unittest.TestCase):
    
    @mock   
    # UPDATE
    def test_update_emp_details(self):
        yeswanth = Employee(1987,'Yeswanth B',8000)
        emp_sal = yeswanth.update_emp_details()
        self.assertEquals(emp_sal,34500,"Sal Hike is Wrong")
if __name__ == '__main__':
    unittest.main()
    
            
    
    

