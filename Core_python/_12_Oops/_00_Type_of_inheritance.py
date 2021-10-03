"""

What Is Inheritance?
====================
The method of inheriting the properties of parent class into a child class is known as inheritance. It is an OOP concept
Following are the benefits of inheritance.

Code re-usability- we do not have to write the same code again and again, we can just inherit the properties
we need in a child class.

It represents a real world relationship between parent class and child class.

It is transitive in nature. If a child class inherits properties from a parent class, then all other sub-classes of the
child class will also inherit the properties of the parent class.

Below is a simple example of inheritance in python.

class Parent():
       def first(self):
           print('first function')

class Child(Parent):
       def second(self):
          print('second function')

ob = Child()
ob.first()
ob.second()


Single Inheritance:
===================
When a child class inherits only a single parent class.

class Parent:
     def func1(self):
          print("this is function one")
class Child(Parent):
     def func2(self):
          print(" this is function 2 ")
ob = Child()
ob.func1()
ob.func2()

Multiple Inheritance:
====================
When a child class inherits from more than one parent class.

class Parent:
   def func1(self):
        print("this is function 1")
class Parent2:
   def func2(self):
        print("this is function 2")
class Child(Parent , Parent2):
    def func3(self):
        print("this is function 3")

ob = Child()
ob.func1()
ob.func2()
ob.func3()

Multilevel Inheritance:
======================
When a child class becomes a parent class for another child class.

class Parent:
      def func1(self):
          print("this is function 1")
class Child(Parent):
      def func2(self):
          print("this is function 2")
class Child2(Child):
      def func3("this is function 3")
ob = Child2()
ob.func1()
ob.func2()
ob.func3()

Hierarchical Inheritance:
=========================
Hierarchical inheritance involves multiple inheritance from the same base or parent class.

class Parent:
      def func1(self):
          print("this is function 1")
class Child(Parent):
      def func2(self):
          print("this is function 2")
class Child2(Parent):
      def func3(self):
          print("this is function 3")

ob = Child()
ob1 = Child2()
ob.func1()
ob.func2()


Hybrid Inheritance:
==================
Hybrid inheritance involves multiple inheritance taking place in a single program.

class Parent:
     def func1(self):
         print("this is function one")

class Child(Parent):
     def func2(self):
         print("this is function 2")

class Child1(Parent):
     def func3(self):
         print(" this is function 3"):

class Child3(Parent , Child1):
     def func4(self):
         print(" this is function 4")

ob = Child3()
ob.func1()


Python Super() Function:
========================
Super function allows us to call a method from the parent class.

class Parent:
     def func1(self):
         print("this is function 1")
class Child(Parent):
     def func2(self):
          Super().func1()
          print("this is function 2")

ob = Child()
ob.func2()

Method Overriding:
=================

You can override a method in python. Look at the example below.

class Parent:
    def func1(self):
        print("this is parent function")

class Child(Parent):
    def func1(self):
        print("this is child function")

ob = Child()
ob.func1()

"""