'''
Created on 02-Feb-2019

@author: VNSquare Tech
'''


class Employee:
    def __init__(self, id, name, sal):
        self.id = id
        self.name = name
        self.sal = sal 
        
    # UPDATE
    def update_emp_details(self):
        if(self.sal>0 and self.sal<=10000):
            hike = self.sal*5/100
        elif(self.sal > 10000 and self.sal <= 25000):
            hike = self.sal*10/100
            
        elif(self.sal > 25000):
            hike = self.sal*15/100
        return self.sal+hike
            
    def get_sal_details(self):
        emp_salary = self.sal
        return emp_salary
    
    def get_emp_details(self):

        return self
    
    
def get_list_values(list1):
    list_output = sorted(list1)
    return list_output        
    