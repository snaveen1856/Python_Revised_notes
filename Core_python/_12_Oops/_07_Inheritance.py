"""
http://www.python-course.eu/python3_inheritance.php
http://www.python-course.eu/inheritance_example.php
"""


class Student:

    def __init__(self, rno, name):
        self.rno = rno
        self.name = name

    def get_details(self):
        print("In student get_class method")


navn = Student(10, "Naveen")
navn.get_details()


class Employee(object):

    def __init__(self, eid, name):
        self.eid = eid
        self.name = name

    def get_emp_details(self):
        print("In Super Class : get_emp_details()")
        # print("Employee details are ", self.eid, " ", self.name)

    def get_info(self):
        print("In Super class : get_info()")


"""    def __add__(self, param):
        print("-----------in sublcass Employee add method---------------")
        return self.eid + param.eid
"""


class SoftwareEmployee(Employee):  # IS - A

    def __init__(self, eid, name, sal):
        Employee.__init__(self, eid, name)  # super().__init__(self, fName, lName)
        self.sal = sal

    def get_sw_emp_details(self):
        print("-------In Sub Class : get_sw_emp_deetailsI()-------------")

    def get_emp_details(self):
        print("In Sub Class : get_emp_details()")


print("*******************************")
kumar = Employee(10, "Kumar")
kumar.get_emp_details()
kumar.get_info()
print("*******************************")
siva = SoftwareEmployee(11, "Shiva", 1000)
siva.get_sw_emp_details()
siva.get_info()
siva.get_emp_details()
siva.m3()

print("*******************************")

vijay = Employee(110, "Vijay Kumar")

vijay.get_emp_details()

print("Object   content is ", vijay)
print("Object   content is ", vijay.__str__())
print("Damu ojbect ", vijay.__str__())
gopi = Employee(111, "Gopi")

# print("Adding 2 objects of employee ", pavan + gopi)    #damu.__add__(gopi)


kumar.get_emp_details()
print("*******************************")
print("Type ", type(kumar))


# MRO - Method Resolution order

class A:
    def m1(self):
        print("In A")


class B:
    def m1(self):
        print("In B")


class C(A, B):
    def m2(self):
        print("In C")


c = C()
c.m1()
