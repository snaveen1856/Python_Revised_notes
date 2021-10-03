"""
Class Variables     --- 1st preference
Instance Variables  --- 2nd preference

    Variables
        Instance V
        Class V
    Methods
        Instance M
        Class M

        Instance V  --> Instance M     TRUE
        Class V     --> Class M        TRUE

        Class V     ---> Instance M    TRUE
        Instance V  ---> Class M       FALSE
"""

print("hello world")


class Employee:
    """
    This class is to get employee information
    """
    # Class Variable
    emp_count = 0  # modifiable + sharable
    office_location = "Whitefield"  # sharable 
    company_name = "ORACLE"  # sharable

    # constructor to initialize instance variables
    def __init__(self, id, name, sal):
        self.id = id
        self.name = name
        self.sal = sal
        Employee.emp_count += 1
        print("Employee count ::  ", Employee.emp_count)

    def get_emp_details(self):
        print("EMP DETAILS ARE : ", self.id, " ", self.name, " ", self.sal)
        print("Emp Count ", Employee.emp_count)

    @classmethod
    def get_emp_count(cls):
        print("Total Employees : ", cls.emp_count, "@", cls.office_location, "@", cls.company_name, " ")


Employee.get_emp_count()

navn = Employee(10, "Sai Naveen", 10000)

navn.get_emp_details()  # OR
Employee.get_emp_details(navn)

Employee.get_emp_details(navn)

Employee.get_emp_count()

kumar = Employee(11, "Kumar", 20000)

kumar.get_emp_details()
Employee.get_emp_count()

print("------------------------------------")

'''
1. Python Interpreter will load the respective class(During module execution)
        1.1 It will initialize the class variables by creating memory for variables

During object creation
    2. __new__ function will be called,receives class name,arguments like (num,string,list,tup,set -- dict)
3.Will create empty object and calls __init__ by passing object(instance) and other arguments
5. Initialize instance variables inside __init__ method

IV ==> IM  YES
CV ==> CM  YES
CV ==> IM  YES
IV ==> CM   NO
'''

'''
class var                 instance var
-------------------------- ----------------------------
- while loading class        - at the time of object creation
- class methods ,i m         - instance methods

++ Within instance methods we can use class variables*****
 within class methods we can't use instance variables
'''

# Built in class attributes '''
print("Employee.__dict__:", Employee.__dict__)
print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)

print("----------------------------------")

# object releated Functions   C R U D
print("Does Naveen has salary : ", hasattr(navn, "sal"))  # R
print("Get name of Naveen     : ", getattr(navn, "name"))  # R
print("Set name of Naveen      : ", setattr(navn, "name", "MAD"))  # U
print("Get name of Naveen    : ", getattr(navn, "name"))
print("Delete Naveen  salary  : ", delattr(navn, "sal"))  # D
print("Delete Naveen  salary  : ", getattr(navn, "sal"))
