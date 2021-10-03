from test.test_heapq import SideEffectLT
from ctypes.test.test_pickling import name


'''
Student
 r_no name   marks   percentage   section   fee school_name school_address student_count  attendance student_address

bank name ifsc code  acc_no name bank_address 

mobile_series mobile_model mobile_no iemi 


Instance variable : Individual to each object
Class variable : Sharable and modifiable by all objects


IV  ----> IM
CV  ----> CM


Assignment :
--------------
IV  ----> CM  ??
CV  ----> IM  ??

'''
'''
Behavior  -- Action -- Fund Transfer

STATE      -- Bank AccNo Name Branch IFSC Code Amount  


Class Object
Encapsulation :  Binding the data members and 
                             member methods into single entity(Class,object)
Abstraction    : Hiding implementation details and exposing only method signature 
                
                
                   
                             Logical     Physical 
                    Class    variables   methods
                    object   methods     variables
                
Abstraction   :      Class          -  0% abstraction
                     Abstract class -  0% to 100% abstraction
                     Interface      - 100%  abstraction 
'''


class Employee1:
    # FIELDS 
    # para constructor

    def __init__(self, eid, name="Naveen", sal=10000):
        self.eid = eid
        self.name = name
        self.sal = sal

    # METHODS
    # INSTANCE METHOD
    def get_emp_hike(self, sal=1000):
        print("----In get employee hike----------")

    # INSTANCE METHOD
    def get_emp_desn(self, hike):
        if self.sal <= 100000:
            print(self.name, " is a software trainee")
        else:
            print(self.name, " is a software engineer")


'''
 1. Class Defined and provided special method i.e, __init__(constructor) method to initialize instance variables, 
    define respective methods to get the BEHAVIOR
2.  Create object for the respective class.
        Internally 
         Python creates empty object for us,and gives reference to self parameter
         Remaining parameters, we are passing the arguments
         In empty object, instance variables will be initialized with the given data
3. Finally whole object reference will be given to LHS
4. We can perform method calls using created object       
    

'''
navn = Employee1(100, "Naveen", 15000)  # Object creation, navn is an object which is of type Employee

print(navn.get_emp_hike())
navn.get_emp_desn()  # Employee.get_emp_desn(navn)

sai = Employee1(200, "sai", 25000)
sai.get_emp_desn()


class Student:
    # FIELDS
    # class variables
    school_name = "ABC"
    school_address = "BANGALORE"
    student_count = 0

    def __init__(self, sid, name, marks):
        self.sid = sid
        self.name = name
        self.marks = marks
        Student.student_count += 1

    # METHODS
    @classmethod
    def get_student_count(cls):
        print("---The student count is :: ", cls.student_count)


Student.get_student_count()

navn = Student()

Student.get_student_count()
'''
class list:
    def __init__(self,*args,**kwargs):
        .....
    
    def append(self):
        
    def pop(self):
        
    ....
'''
list1 = [1, 2, 3, 4]
list1 = list([1, 2, 3, 4])
print(list1.append([2, 4]))

# class method calling
Employee1.emp_count()

navn = Employee1(10, "Naveen", 1000)
print(navn)
list1 = [1, 2, 3]
print(list1)
# instance method calling
navn.get_emp_details()
Employee1.get_emp_details(navn)
# print("---------Normal Instance calling-------------")

# sai = Employee(21,"Sai kumar",15000)
# sai.get_emp_details()

'''

class var                 instance var
-------------------------- ----------------------------
while loading class        at the time of object creation

class var                  instance var
class methods              instance methods

No instance var inside class method**

++ Within instance methods we can use class variables*****
vice versa is not True ==> within class methods we can't use instance variables
'''
# Built in class attributes '''
print("Employee.__dict__:", Employee1.__dict__)
print("Employee.__doc__:", Employee1.__doc__)
print("Employee.__name__:", Employee1.__name__)
print("Employee.__module__:", Employee1.__module__)
print("Employee.__bases__:", Employee1.__bases__)

# Functions
print(hasattr(navn, "sal"))
print(setattr(navn, "name", "MAD"))
print(getattr(navn, "name"))


# print(delattr(navn, "sal"))
# print(getattr(navn, "sal"))


class Employee:
    def __init__(self, x):
        print(x)
        # return x


c = Employee(5)
