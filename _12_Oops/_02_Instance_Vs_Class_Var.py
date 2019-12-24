"""
#---------------------BEFORE----------------------
print("---------------------BEFORE----------------------")
class Employee:
    def __init__(self, eid, name, sal, office_name = "ORACLE"):
        self.eid = eid
        self.name = name
        self.sal = sal
        self.office_name = office_name

    # METHODS
    def get_emp_hike(self):
        print("----In get employee hike----------")

    def get_emp_desn(self):
        if(self.sal <= 15000):
            print(self.name, " is a software trainee, office is :",self.office_name)
        else:
            print(self.name, " is a software engineer office is :",self.office_name)

navn = Employee(100,"Naveen",10000)  # Object creation, navn is an object which is of type Employee
navn.get_emp_desn()  # Employee.get_emp_desn(navn)

sai = Employee(200,"sai",25000)
sai.get_emp_desn()

print("---------------------BEFORE----------------------")
"""


class Employee:
    # class variables
    office_name = "ORACLE"  # Class Variable  1. Sharable
    emp_count = 0  # 2. Sharable + Modifiable

    # constructor   # instance variables
    def __init__(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal
        Employee.emp_count += 1

    # METHODS
    # INSTANCE METHOD
    def get_emp_hike(self):
        print("----In get employee hike----------")

    # INSTANCE METHOD
    def get_emp_desn(self):
        if self.sal <= 15000:
            print(self.name, " is a software trainee and his company name is ", Employee.office_name)
        else:
            print(self.name, " is a software engineer and his company name is ", Employee.office_name)


'''
1. Class Defined and provided special method i.e, __init__(constructor) method to initialize instance variables, 
    define respective methods to get the BEHAVIOR
2.  Create object for the respective class.
        Internally 
         - Python creates empty object for us,and gives reference to "self" parameter
         - Remaining parameters, we are passing as arguments
         - In empty object, instance variables will be initialized with the given data
3. Finally whole object reference will be given to LHS(object/instance,variable)
4. We can perform method calls using created object
'''

print("-----Employee count ---Company start-------", Employee.emp_count)

navn = Employee(100, "Naveen", 10000)  # Object creation, navn is an object which is of type Employee

print("-----Employee count --navn--------", Employee.emp_count)
print(Employee.office_name)
print(navn.get_emp_hike())
navn.get_emp_desn()  # Employee.get_emp_desn(navn)

sai = Employee(200, "sai", 25000)
print("-----Employee count ---sai-------", Employee.emp_count)
sai.get_emp_desn()
